from fastapi import Depends

from backend.database.models import DummyTestDB
from backend.repository.dummy_test import DummyTestRepository
from backend.schemas.dummy_test import DummyTestCreate


class DummyTestService:
    """
    This service is used only for testing purposes
    """

    def __init__(self, dummy_repository: DummyTestRepository = Depends()):
        self._dummy_repository = dummy_repository

    def create(self, dummy: DummyTestCreate) -> DummyTestDB:
        return self._dummy_repository.insert(dummy)
