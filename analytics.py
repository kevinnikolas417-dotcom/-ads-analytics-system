"""Serviço de análise de campanhas"""
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
from config import get_settings

logger = logging.getLogger(__name__)

@dataclass
class CampaignAnalysis:
    campaign_id: str
    campaign_name: str
    total_spend: float
    total_revenue: float
    total_impressions: int
    total_clicks: int
    total_conversions: int
    roi: float
    roas: float
    ctr: float
    cpc: float
    cpm: float
    cpa: float
    trend: str
    health_score: float
    recommendations: List[str]

class AnalyticsService:
    """Serviço para análise de campanhas"""
    def __init__(self):
        self.settings = get_settings()

    def calculate_roi(self, revenue: float, spend: float) -> float:
        if spend == 0:
            return 0.0
        return ((revenue - spend) / spend) * 100

    def calculate_roas(self, revenue: float, spend: float) -> float:
        if spend == 0:
            return 0.0
        return revenue / spend

    def calculate_ctr(self, clicks: int, impressions: int) -> float:
        if impressions == 0:
            return 0.0
        return (clicks / impressions) * 100

    def calculate_cpc(self, spend: float, clicks: int) -> float:
        if clicks == 0:
            return 0.0
        return spend / clicks

    def calculate_cpm(self, spend: float, impressions: int) -> float:
        if impressions == 0:
            return 0.0
        return (spend / impressions) * 1000

    def calculate_cpa(self, spend: float, conversions: int) -> float:
        if conversions == 0:
            return 0.0
        return spend / conversions

    def calculate_health_score(self, roi: float, roas: float, ctr: float, spend: float, conversions: int) -> float:
        score = 0.0
        if roi >= self.settings.GOOD_ROI_THRESHOLD:
            score += 30
        else:
            score += (roi / self.settings.GOOD_ROI_THRESHOLD) * 30
        if roas >= self.settings.GOOD_ROAS_THRESHOLD:
            score += 30
        else:
            score += (roas / self.settings.GOOD_ROAS_THRESHOLD) * 30
        if ctr >= self.settings.GOOD_CTR_THRESHOLD:
            score += 20
        else:
            score += (ctr / self.settings.GOOD_CTR_THRESHOLD) * 20
        if conversions >= 10:
            score += 20
        elif conversions >= 5:
            score += 15
        elif conversions >= 1:
            score += 10
        return min(score, 100.0)

    def generate_recommendations(self, campaign_analysis: CampaignAnalysis) -> List[Dict]:
        recommendations = []
        if campaign_analysis.roi < 0:
            recommendations.append({"type": "NEGATIVE_ROI", "title": "⚠️ ROI Negativo", "description": "Esta campanha está tendo ROI negativo.", "priority": "HIGH"})
        elif campaign_analysis.roi < self.settings.GOOD_ROI_THRESHOLD:
            recommendations.append({"type": "LOW_ROI", "title": "📈 Aumentar ROI", "description": f"ROI está em {campaign_analysis.roi:.1f}%", "priority": "MEDIUM"})
        if campaign_analysis.health_score >= 80:
            recommendations.append({"type": "SCALE_BUDGET", "title": "🚀 Escalar Campanha", "description": "Campanha com excelente desempenho", "priority": "HIGH"})
        return recommendations

    def get_benchmark_metrics(self) -> Dict:
        return {"good_roi_threshold": self.settings.GOOD_ROI_THRESHOLD, "good_roas_threshold": self.settings.GOOD_ROAS_THRESHOLD, "good_ctr_threshold": self.settings.GOOD_CTR_THRESHOLD}
