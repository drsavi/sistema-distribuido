from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database import get_sessions
from backend.database.models import FilmeDB
from backend.schemas.filme_schema import FilmeCreate
from sqlalchemy import update as sql_update


class FilmeRepository:
#    def __init__(self, base_repository: Session = Depends(get_sessions)):
#        self._session = base_repository

    def insert(self, dummy: FilmeCreate) -> FilmeDB:
#        obj_db = FilmeDB(**dummy.dict())
#        self._session.add(obj_db)
#        return obj_db
        return FilmeDB(**dummy.dict())

#    def update(self, dummy_id: int, dummy: FilmeCreate) -> FilmeDB:
#        dummy = (
#            sql_update(FilmeDB).
#            where(FilmeDB.id == dummy_id).
#            values(**dummy.dict())
#        )

#        return dummy
