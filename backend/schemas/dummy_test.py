"""
These Models are used only for testing purposes
"""
from pydantic import BaseModel

from backend.schemas import CRUDModel, OrmModel


class DummyTestBase(BaseModel):
    attribute: str


class DummyTest(DummyTestBase, OrmModel):
    ...


class DummyTestCreate(DummyTestBase, CRUDModel):
    ...


class DummyTestInternal(DummyTest):
    id: int
