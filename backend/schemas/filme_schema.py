"""
These Models are used only for ing purposes
"""
from pydantic import BaseModel

from backend.schemas import CRUDModel, OrmModel


class FilmeBase(BaseModel):
    title: str
    director: str


class Filme(FilmeBase, OrmModel):
    ...


class FilmeCreate(FilmeBase, CRUDModel):
    ...


class FilmeInternal(Filme):
    id: int
