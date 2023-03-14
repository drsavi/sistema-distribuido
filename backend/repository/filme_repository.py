from typing import List
from backend.database.models import FilmeDB
from backend.schemas.filme_schema import FilmeCreate
import redis

class FilmeRepository:

    _filmes = []

    def insert(self, dummy: FilmeCreate) -> FilmeDB:
        filme = FilmeDB(**dummy.dict())
        self._filmes.append(filme)
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set(filme.title, filme)
        return filme
        
    def get_all(self) -> List[FilmeDB]:
        r = redis.Redis(host='localhost', port=6379, db=0)
        filmes = []
        for title in r.keys():
            filme = r.get(title)
            filmes.append(filme)
        return filmes
