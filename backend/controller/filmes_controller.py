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
def create(dummy: FilmeCreate, dummy_service: FilmeService = Depends()) -> FilmeDB:
    return dummy_service.create(dummy)
