from core.models.credential import Crendential
from core.models.session import Session
from core.ports.auth_repository import AuthRepositoryInterface
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
create conections to sql lite
"""


class MysqlAuthRepository(AuthRepositoryInterface):
    def __init__(self, SQLITE_DATABASE_URL: str, ):
        self.sqlite_database_url = SQLITE_DATABASE_URL
        engine = create_engine(
            self.sqlite_database_url, echo=True, connect_args={"check_same_thread": False}
        )
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = SessionLocal

        Base = declarative_base()
        self.base = Base

    def validate_credential(self, credential: Crendential) -> Session:
        pass
