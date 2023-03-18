import pickle
from typing import List
from backend.database.models import FilmeDB
from backend.schemas.filme_schema import FilmeCreate
import redis
from pymongo import MongoClient


class FilmeRepository:

    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['filme_db']
        self._collection = self._db['filme']

    def insert(self, filme: FilmeCreate) -> FilmeDB:
        filme = FilmeDB(**filme.dict())
        filme_dict = {
            "title": filme.title,
            "director": filme.director,
            "duration": filme.duration,
        }
        result = self._collection.insert_one(filme_dict)
        filme.id = str(result.inserted_id)
        return filme

    
    def get_all(self) -> List[FilmeDB]:
        filmes = []
        for filme_dict in self._collection.find():
            filme = FilmeDB(
                id=str(filme_dict["_id"]),
                title=filme_dict["title"],
                director=filme_dict["director"],
                duration=filme_dict["duration"],
            )
            filmes.append(filme)
        return filmes
