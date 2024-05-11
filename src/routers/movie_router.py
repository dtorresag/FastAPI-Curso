from fastapi import FastAPI, Body, Path, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from typing import Optional, List
from src.models.movie_model import Movie, MovieCreate, MovieUpdate


movie_router = APIRouter()

movies:List[Movie] = []

@movie_router.get('/', tags=['Movies'])

def get_movies() -> List[Movie]:
    content = [movie.model_dump for movie in movies]
    return JSONResponse(content=content)

@movie_router.get('/{id}', tags=['Movies'])

def get_movie(id:int = Path(gt = 0)) -> Movie:
    for movie in movies:
        if movie.id == id:
            return movie.model_dump
    return {}

@movie_router.post('/', tags=['Movies'])

def create_movie(movie:MovieCreate) -> List[Movie]:
    
    movies.append(movie)
    
    #return [movie.model_dump for movie in movies]
    return  RedirectResponse('/movies', status_code=303)
    

@movie_router.put('/{id}', tags=['Movies'])

def update_movie(id:int, movie:MovieUpdate) -> List[Movie]:
    for m in movies:
        if m.id == id:
            m.title = movie.title
            m.overview = movie.overview
            m.year = movie.year
    return [movie.model_dump for movie in movies]