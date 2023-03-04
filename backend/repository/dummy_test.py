from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database import get_sessions
from backend.database.models import DummyTestDB
from backend.schemas.dummy_test import DummyTestCreate
from sqlalchemy import update as sql_update


class DummyTestRepository:
#    def __init__(self, base_repository: Session = Depends(get_sessions)):
#        self._session = base_repository

    def insert(self, dummy: DummyTestCreate) -> DummyTestDB:
#        obj_db = DummyTestDB(**dummy.dict())
#        self._session.add(obj_db)
#        return obj_db
        return DummyTestDB(**dummy.dict())

#    def update(self, dummy_id: int, dummy: DummyTestCreate) -> DummyTestDB:
#        dummy = (
#            sql_update(DummyTestDB).
#            where(DummyTestDB.id == dummy_id).
#            values(**dummy.dict())
#        )

#        return dummy
