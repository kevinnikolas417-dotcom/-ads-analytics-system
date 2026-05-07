"""Integração com Meta Marketing API"""
import requests
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from config import get_settings

logger = logging.getLogger(__name__)

class MetaAPI:
    """Cliente para Meta Marketing API"""
    BASE_URL = "https://graph.instagram.com/v18.0"
    GRAPH_URL = "https://graph.facebook.com/v18.0"

    def __init__(self):
        self.settings = get_settings()
        self.access_token = self.settings.FACEBOOK_ACCESS_TOKEN
        self.business_account_id = self.settings.FACEBOOK_BUSINESS_ACCOUNT_ID

    def _get_headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}

    def _make_request(self, method: str, url: str, **kwargs) -> Optional[Dict]:
        try:
            headers = self._get_headers()
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição Meta API: {str(e)}")
            return None

    def get_campaigns(self, account_id: Optional[str] = None) -> List[Dict]:
        if not account_id:
            account_id = self.business_account_id
        url = f"{self.GRAPH_URL}/{account_id}/campaigns"
        params = {"access_token": self.access_token, "fields": "id,name,status,objective,budget,created_time,updated_time"}
        logger.info(f"Buscando campanhas da conta {account_id}")
        response = self._make_request("GET", url, params=params)
        if response and "data" in response:
            logger.info(f"✅ {len(response['data'])} campanhas encontradas")
            return response["data"]
        return []

    def get_campaign_metrics(self, campaign_id: str, date_from: Optional[str] = None, date_to: Optional[str] = None) -> List[Dict]:
        if not date_from:
            date_from = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d")
        if not date_to:
            date_to = datetime.utcnow().strftime("%Y-%m-%d")
        url = f"{self.GRAPH_URL}/{campaign_id}/insights"
        params = {"access_token": self.access_token, "fields": "campaign_id,campaign_name,date_start,date_stop,impressions,clicks,spend,actions,action_values,ctr,cpc,cpm", "date_preset": "last_7d"}
        logger.info(f"Buscando métricas da campanha {campaign_id}")
        response = self._make_request("GET", url, params=params)
        if response and "data" in response:
            logger.info(f"✅ {len(response['data'])} registros de métricas encontrados")
            return response["data"]
        return []

    def get_ad_sets(self, campaign_id: str) -> List[Dict]:
        url = f"{self.GRAPH_URL}/{campaign_id}/adsets"
        params = {"access_token": self.access_token, "fields": "id,name,status,budget,daily_budget,targeting,created_time,updated_time"}
        logger.info(f"Buscando Ad Sets da campanha {campaign_id}")
        response = self._make_request("GET", url, params=params)
        if response and "data" in response:
            logger.info(f"✅ {len(response['data'])} Ad Sets encontrados")
            return response["data"]
        return []

    def get_ads(self, adset_id: str) -> List[Dict]:
        url = f"{self.GRAPH_URL}/{adset_id}/ads"
        params = {"access_token": self.access_token, "fields": "id,name,status,creative,created_time,updated_time"}
        logger.info(f"Buscando Ads do Ad Set {adset_id}")
        response = self._make_request("GET", url, params=params)
        if response and "data" in response:
            logger.info(f"✅ {len(response['data'])} Ads encontrados")
            return response["data"]
        return []

    def test_connection(self) -> bool:
        logger.info("Testando conexão com Meta API...")
        url = f"{self.GRAPH_URL}/me"
        params = {"access_token": self.access_token}
        response = self._make_request("GET", url, params=params)
        if response and "id" in response:
            logger.info(f"✅ Conexão bem-sucedida! User ID: {response['id']}")
            return True
        logger.error("❌ Falha na conexão com Meta API")
        return False
