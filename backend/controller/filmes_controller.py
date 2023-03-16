from typing import List
from fastapi import APIRouter, Depends

from backend.database.models import FilmeDB
from backend.schemas.filme_schema import Filme, FilmeCreate
from backend.service.filme_service import FilmeService

singular = APIRouter(prefix="/filme")

@singular.post(
    "/",
    summary="Endpoint para cadastro de filme",
    description="Este endpoint serve para cadastrar um filme",
    response_model=Filme,
)
def create(filme: FilmeCreate, filme_service: FilmeService = Depends()) -> FilmeDB:
    return filme_service.create(filme)


@singular.get(
    "/",
    summary="Endpoint para retornar a lista de filmes cadastrados ",
    description="Este endpoint serve para retornar a lista de filmes cadastrados",
    response_model=List[Filme],
)
def get_all(dummy_service: FilmeService = Depends()) -> List[Filme]:
    return dummy_service.get_all()
