from fastapi import APIRouter, Depends

from backend.database.models import DummyTestDB
from backend.schemas.dummy_test import DummyTest, DummyTestCreate
from backend.service.dummy_test import DummyTestService

singular = APIRouter(prefix="/dummy_test")


@singular.post(
    "/",
    summary="Dummy test endpoint",
    description="Dummy endpoint used only for testing purposes",
    response_model=DummyTest,
)
def create(dummy: DummyTestCreate, dummy_service: DummyTestService = Depends()) -> DummyTestDB:
    return dummy_service.create(dummy)
