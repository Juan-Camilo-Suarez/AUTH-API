from core.models.credential import Crendential
from core.models.session import Session
from core.ports.auth_repository import AuthRepositoryInterface


class MysqlAuthRepository(AuthRepositoryInterface):

    def validate_credential(self, credential: Crendential) -> Session:
        pass
