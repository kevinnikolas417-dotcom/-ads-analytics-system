"""
API FastAPI para Sistema de Análise de Campanhas
"""
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from config import get_settings
from meta_api import MetaAPI
from analytics import AnalyticsService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Ad Analytics System", description="Sistema de análise e otimização de campanhas Facebook/Instagram", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

settings = get_settings()
meta_api = MetaAPI()
analytics_service = AnalyticsService()

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Iniciando Sistema de Análise de Campanhas")
    if settings.validate():
        if meta_api.test_connection():
            logger.info("✅ Conexão com Meta API estabelecida")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat(), "version": "1.0.0"}

@app.get("/api/campaigns")
async def get_campaigns():
    try:
        campaigns = meta_api.get_campaigns()
        if not campaigns:
            raise HTTPException(status_code=404, detail="Nenhuma campanha encontrada")
        return {"total": len(campaigns), "campaigns": campaigns}
    except Exception as e:
        logger.error(f"Erro ao buscar campanhas: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao buscar campanhas")

@app.get("/api/analysis/health-scores")
async def get_health_scores():
    try:
        campaigns = meta_api.get_campaigns()
        if not campaigns:
            raise HTTPException(status_code=404, detail="Nenhuma campanha encontrada")
        health_scores = []
        for campaign in campaigns:
            metrics = meta_api.get_campaign_metrics(campaign["id"])
            if metrics:
                total_spend = sum(m.get("spend", 0) for m in metrics)
                total_revenue = sum(m.get("actions", [{}])[0].get("value", 0) if m.get("actions") else 0 for m in metrics)
                total_clicks = sum(m.get("clicks", 0) for m in metrics)
                total_impressions = sum(m.get("impressions", 0) for m in metrics)
                roi = analytics_service.calculate_roi(total_revenue, total_spend)
                roas = analytics_service.calculate_roas(total_revenue, total_spend)
                ctr = analytics_service.calculate_ctr(total_clicks, total_impressions)
                health_score = analytics_service.calculate_health_score(roi=roi, roas=roas, ctr=ctr, spend=total_spend, conversions=len(metrics))
                health_scores.append({"campaign_id": campaign["id"], "campaign_name": campaign.get("name", "Unknown"), "health_score": health_score, "roi": roi, "roas": roas, "ctr": ctr})
        health_scores.sort(key=lambda x: x["health_score"], reverse=True)
        return {"total_campaigns": len(health_scores), "health_scores": health_scores, "generated_at": datetime.utcnow().isoformat()}
    except Exception as e:
        logger.error(f"Erro ao calcular health scores: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao calcular health scores")

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    with open("dashboard.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/export/metrics")
async def export_metrics_json():
    try:
        campaigns = meta_api.get_campaigns()
        all_data = []
        for campaign in campaigns:
            metrics = meta_api.get_campaign_metrics(campaign["id"])
            all_data.append({"campaign": campaign, "metrics": metrics})
        return {"status": "success", "total_campaigns": len(all_data), "data": all_data, "exported_at": datetime.utcnow().isoformat()}
    except Exception as e:
        logger.error(f"Erro ao exportar métricas: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao exportar métricas")

@app.post("/api/sync/campaigns")
async def sync_campaigns():
    try:
        logger.info("Iniciando sincronização de campanhas...")
        campaigns = meta_api.get_campaigns()
        sync_count = len(campaigns)
        logger.info(f"✅ Sincronização concluída: {sync_count} campanhas")
        return {"status": "success", "campaigns_synced": sync_count, "timestamp": datetime.utcnow().isoformat()}
    except Exception as e:
        logger.error(f"Erro durante sincronização: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro durante sincronização")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
