from fastapi import APIRouter

from backend.controller import filmes_controller

router = APIRouter(prefix="/api")
router.include_router(filmes_controller.singular)
