"""Configurações da aplicação"""
import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class Settings:
    """Configurações principais da aplicação"""
    FACEBOOK_ACCESS_TOKEN: str = os.getenv("FACEBOOK_ACCESS_TOKEN", "")
    FACEBOOK_APP_ID: str = os.getenv("FACEBOOK_APP_ID", "")
    FACEBOOK_APP_SECRET: str = os.getenv("FACEBOOK_APP_SECRET", "")
    FACEBOOK_BUSINESS_ACCOUNT_ID: str = os.getenv("FACEBOOK_BUSINESS_ACCOUNT_ID", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ads_db.db")
    DATABASE_POOL_SIZE: int = int(os.getenv("DATABASE_POOL_SIZE", "20"))
    DATABASE_MAX_OVERFLOW: int = int(os.getenv("DATABASE_MAX_OVERFLOW", "10"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    PORT: int = int(os.getenv("PORT", "8000"))
    HOST: str = os.getenv("HOST", "0.0.0.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    COLLECTION_INTERVAL_MINUTES: int = int(os.getenv("COLLECTION_INTERVAL_MINUTES", "60"))
    DATA_START_DATE: str = os.getenv("DATA_START_DATE", "")
    GOOD_ROI_THRESHOLD: float = float(os.getenv("GOOD_ROI_THRESHOLD", "150"))
    GOOD_ROAS_THRESHOLD: float = float(os.getenv("GOOD_ROAS_THRESHOLD", "2.5"))
    GOOD_CTR_THRESHOLD: float = float(os.getenv("GOOD_CTR_THRESHOLD", "2.0"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "logs/app.log")

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"

    def validate(self) -> bool:
        required = ["FACEBOOK_ACCESS_TOKEN", "FACEBOOK_APP_ID", "FACEBOOK_APP_SECRET", "FACEBOOK_BUSINESS_ACCOUNT_ID"]
        missing = [field for field in required if not getattr(self, field, None)]
        if missing:
            print(f"❌ Configurações obrigatórias faltando: {', '.join(missing)}")
            return False
        print("✅ Todas as configurações obrigatórias estão presentes")
        return True

@lru_cache()
def get_settings() -> Settings:
    return Settings()
