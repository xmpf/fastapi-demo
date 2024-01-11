from fastapi import (
    FastAPI,
)

# from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from app.middlewares import (
    add_cors_middleware,
    add_csp_middleware,
)

from app.routers.tasks import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("BEFORE")
    yield
    print("AFTER")

app = FastAPI(lifespan=lifespan)

# app.mount("/static", StaticFiles(directory="static"), name="static")

add_cors_middleware(app=app)
# add_csp_middleware(app=app)

app.include_router(router=tasks_router, tags=["tasks"], prefix="/tasks")