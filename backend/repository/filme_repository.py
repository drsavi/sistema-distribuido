from typing import List
from backend.database.models import FilmeDB
from backend.schemas.filme_schema import FilmeCreate

class FilmeRepository:

    _filmes = []

    def insert(self, dummy: FilmeCreate) -> FilmeDB:
        filme = FilmeDB(**dummy.dict())
        self._filmes.append(filme)
        return filme
        
    def get_all(self) -> List[FilmeDB]:
        return self._filmes 