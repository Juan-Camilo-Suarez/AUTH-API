from core.models.session import Session
from core.models.credential import Crendential


class AuthRepositoryInterface:
    def validate_credential(self, credential: Crendential) -> Session:
        pass
