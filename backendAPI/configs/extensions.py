from typing import Any, Dict
from sqlalchemy import MetaData
from configs.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
# Database
metadata = MetaData()
dbModel = declarative_base(metadata = metadata)

# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_recycle=3600, echo=True)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DBSession = SessionLocal()

# Logging configuration
def configure_logging(logConfig: Dict[str, Any]) -> Dict[str, Any]:
    datefmt = '%d-%m-%Y %H:%M:%S'
    formatters = logConfig['formatters']
    formatters['default']['fmt'] = '[%(asctime)s] %(levelprefix)s %(message)s'
    formatters['access']['fmt'] = '[%(asctime)s] %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'
    formatters['access']['datefmt'] = datefmt
    formatters['default']['datefmt'] = datefmt
    formatters['access']['use_colors'] = True
    formatters['default']['use_colors'] = True
    return logConfig

