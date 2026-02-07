from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import engine
from models import Base
from routers.movies import router as movie_router
from routers.users import router as user_router

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router)
app.include_router(movie_router)
