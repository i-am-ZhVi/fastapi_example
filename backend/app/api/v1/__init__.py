from fastapi import APIRouter


router = APIRouter(prefix="/v1")

from .endpoints import (
    users_router,
    walls_router,
    private_messages_router,
    messages_router,
    friends_router,
    files_router,
)

router.include_router(users_router)
router.include_router(walls_router)
router.include_router(private_messages_router)
router.include_router(messages_router)
router.include_router(friends_router)
router.include_router(files_router)
