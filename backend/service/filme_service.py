from typing import List
from fastapi import Depends
from backend.database.models import FilmeDB
from backend.repository.filme_repository import FilmeRepository
from backend.schemas.filme_schema import FilmeCreate

class FilmeService:

    def __init__(self, dummy_repository: FilmeRepository = Depends()):
        self._dummy_repository = dummy_repository

    def create(self, dummy: FilmeCreate) -> FilmeDB:
        return self._dummy_repository.insert(dummy)

    def get_all(self) -> List[FilmeDB]:
        return self._dummy_repository.get_all()
    
