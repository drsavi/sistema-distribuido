from fastapi import APIRouter

from backend.controller import dummy_test
from backend.controller import filmes_controller

router = APIRouter(prefix="/api")
router.include_router(dummy_test.singular)
router.include_router(filmes_controller.singular)
