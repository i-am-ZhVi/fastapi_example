from fastapi import APIRouter


router = APIRouter(prefix="/v1")

from .endpoints import (
    users_router,
)

router.include_router(users_router)
