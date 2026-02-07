from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Movie
from schemas import MovieCreate, MovieRead
from database import get_db

router = APIRouter()

@router.get("/movies/{movie_id}", response_model=MovieRead)
async def get_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    movie = result.scalar_one_or_none()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/movies/", response_model=MovieRead)
async def create_movie(film: MovieCreate, db: AsyncSession = Depends(get_db)):
    new_movie = Movie(**film.model_dump())
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)
    return new_movie
