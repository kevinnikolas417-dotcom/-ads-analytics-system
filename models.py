"""Modelos de banco de dados"""
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True)
    facebook_campaign_id = Column(String(100), unique=True, index=True)
    name = Column(String(255))
    status = Column(String(50))
    objective = Column(String(100))
    budget = Column(Float, default=0.0)
    budget_currency = Column(String(3), default="USD")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_synced = Column(DateTime)
    ad_sets = relationship("AdSet", back_populates="campaign", cascade="all, delete-orphan")
    metrics = relationship("CampaignMetric", back_populates="campaign", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="campaign", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Campaign {self.name}>"

class AdSet(Base):
    __tablename__ = "ad_sets"
    id = Column(Integer, primary_key=True)
    facebook_adset_id = Column(String(100), unique=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    name = Column(String(255))
    status = Column(String(50))
    budget = Column(Float, default=0.0)
    daily_budget = Column(Float, default=0.0)
    targeting = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    campaign = relationship("Campaign", back_populates="ad_sets")
    ads = relationship("Ad", back_populates="ad_set", cascade="all, delete-orphan")
    metrics = relationship("AdSetMetric", back_populates="ad_set", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<AdSet {self.name}>"

class Ad(Base):
    __tablename__ = "ads"
    id = Column(Integer, primary_key=True)
    facebook_ad_id = Column(String(100), unique=True, index=True)
    ad_set_id = Column(Integer, ForeignKey("ad_sets.id"), nullable=False)
    name = Column(String(255))
    status = Column(String(50))
    creative_data = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ad_set = relationship("AdSet", back_populates="ads")
    metrics = relationship("AdMetric", back_populates="ad", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Ad {self.name}>"

class CampaignMetric(Base):
    __tablename__ = "campaign_metrics"
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    date = Column(DateTime, index=True)
    impressions = Column(Integer, default=0)
    reach = Column(Integer, default=0)
    frequency = Column(Float, default=0.0)
    clicks = Column(Integer, default=0)
    ctr = Column(Float, default=0.0)
    spend = Column(Float, default=0.0)
    cpc = Column(Float, default=0.0)
    cpm = Column(Float, default=0.0)
    conversions = Column(Integer, default=0)
    cpa = Column(Float, default=0.0)
    conversion_rate = Column(Float, default=0.0)
    revenue = Column(Float, default=0.0)
    roi = Column(Float, default=0.0)
    roas = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    campaign = relationship("Campaign", back_populates="metrics")

    def __repr__(self):
        return f"<CampaignMetric campaign_id={self.campaign_id} date={self.date}>"

class AdSetMetric(Base):
    __tablename__ = "adset_metrics"
    id = Column(Integer, primary_key=True)
    ad_set_id = Column(Integer, ForeignKey("ad_sets.id"), nullable=False)
    date = Column(DateTime, index=True)
    impressions = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    ctr = Column(Float, default=0.0)
    spend = Column(Float, default=0.0)
    cpc = Column(Float, default=0.0)
    conversions = Column(Integer, default=0)
    cpa = Column(Float, default=0.0)
    revenue = Column(Float, default=0.0)
    roi = Column(Float, default=0.0)
    roas = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    ad_set = relationship("AdSet", back_populates="metrics")

    def __repr__(self):
        return f"<AdSetMetric ad_set_id={self.ad_set_id}>"

class AdMetric(Base):
    __tablename__ = "ad_metrics"
    id = Column(Integer, primary_key=True)
    ad_id = Column(Integer, ForeignKey("ads.id"), nullable=False)
    date = Column(DateTime, index=True)
    impressions = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    ctr = Column(Float, default=0.0)
    spend = Column(Float, default=0.0)
    cpc = Column(Float, default=0.0)
    conversions = Column(Integer, default=0)
    cpa = Column(Float, default=0.0)
    revenue = Column(Float, default=0.0)
    roi = Column(Float, default=0.0)
    roas = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    ad = relationship("Ad", back_populates="metrics")

    def __repr__(self):
        return f"<AdMetric ad_id={self.ad_id}>"

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    title = Column(String(255))
    description = Column(Text)
    recommendation_type = Column(String(50))
    priority = Column(String(20))
    potential_impact = Column(String(100))
    is_implemented = Column(Boolean, default=False)
    implemented_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    campaign = relationship("Campaign", back_populates="recommendations")

    def __repr__(self):
        return f"<Recommendation {self.recommendation_type}>"

class SyncLog(Base):
    __tablename__ = "sync_logs"
    id = Column(Integer, primary_key=True)
    sync_type = Column(String(50))
    status = Column(String(20))
    message = Column(Text)
    campaigns_synced = Column(Integer, default=0)
    adsets_synced = Column(Integer, default=0)
    ads_synced = Column(Integer, default=0)
    started_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime)
    duration_seconds = Column(Integer)

    def __repr__(self):
        return f"<SyncLog {self.sync_type} - {self.status}>"
