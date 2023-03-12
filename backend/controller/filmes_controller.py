from typing import List
import requests
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


def send_message_to_another_service(self, message: str):
    url = "http://localhost:8081/messages"
    payload = {"message": message}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error sending message:", response.status_code)

        
@singular.post(
    "/send_message_to_another_service",
    summary="Endpoint para enviar mensagem para outro serviço",
    description="Este endpoint serve para enviar uma mensagem para outro serviço",
)
def send_message_to_another_service(message: str, filme_service: FilmeService = Depends()):
    filme_service.send_message_to_another_service(message)
    return {"message": "Message sent successfully!"}

