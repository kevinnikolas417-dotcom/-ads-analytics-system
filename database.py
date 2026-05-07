"""Inicialização e gerenciamento do banco de dados"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_settings
from models import Base

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.settings = get_settings()
        self.engine = None
        self.SessionLocal = None

    def initialize(self):
        logger.info("Inicializando banco de dados...")
        try:
            self.engine = create_engine(self.settings.DATABASE_URL, pool_size=self.settings.DATABASE_POOL_SIZE, max_overflow=self.settings.DATABASE_MAX_OVERFLOW, echo=self.settings.DEBUG)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            Base.metadata.create_all(bind=self.engine)
            logger.info("✅ Banco de dados inicializado com sucesso")
            return True
        except Exception as e:
            logger.error(f"❌ Erro ao inicializar banco de dados: {str(e)}")
            return False

    def get_session(self):
        if not self.SessionLocal:
            self.initialize()
        return self.SessionLocal()

    def close(self):
        if self.engine:
            self.engine.dispose()
            logger.info("Conexão com banco de dados fechada")

    def health_check(self) -> bool:
        try:
            session = self.get_session()
            session.execute("SELECT 1")
            session.close()
            return True
        except Exception as e:
            logger.error(f"Falha na verificação de saúde do BD: {str(e)}")
            return False

db = Database()

def get_db():
    session = db.get_session()
    try:
        yield session
    finally:
        session.close()

def init_db():
    logger.info("🗄️  Inicializando banco de dados...")
    db.initialize()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    init_db()
