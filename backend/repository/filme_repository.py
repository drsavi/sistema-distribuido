import pickle
from typing import List
from backend.database.models import FilmeDB
from backend.schemas.filme_schema import FilmeCreate
import redis

class FilmeRepository:

    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)

    def insert(self, filme: FilmeCreate) -> FilmeDB:
        filme = FilmeDB(**filme.dict())
        self._redis.set(filme.title, pickle.dumps(filme))
        return filme
        
    def get_all(self) -> List[FilmeDB]:
        filmes = []
        for title in self._redis.keys():
            filme = pickle.loads(self._redis.get(title))
            filmes.append(filme)
        return filmes