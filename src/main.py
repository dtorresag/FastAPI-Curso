from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.requests import Request
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HttpErrorHandler

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os


app = FastAPI()

app.add_middleware(HttpErrorHandler)
#@app.middleware('http')
#async def Http_Error_Handler(request:Request,call_next)-> Response | JSONResponse:
#    try:
#           return await call_next(Request)
#    except Exception as e:
#        content = f"exc {str(e)}"
#        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#        return JSONResponse(content=content, status_code=status_code)

#Se pueden agrupar end points mediante tags

static_path = os.path.join(os.path.dirname(__file__),'static/')
templates_path = os.path.join(os.path.dirname(__file__),'templates/')

app.mount('/static',StaticFiles(directory=static_path), 'static')
templates = Jinja2Templates(directory=templates_path)


@app.get('/', tags=['Home'])

def home(request: Request):
    return templates.TemplateResponse('index.html', {'request':request, 'message':'Welcome'})

app.include_router(prefix='/movies',router=movie_router)