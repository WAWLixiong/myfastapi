"""
path paremeter
predefined value
"""

import time

from fastapi import FastAPI
from fastapi import Request, status, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from auth import authentication
from client import html
from db import models
from db.database import engine
from exceptions import StoryException
from router import blog_get, blog_post, user, article, product, file, dependencies
from templates import templates

app = FastAPI()

app.include_router(authentication.router)  # 应该放在最上边，使用最频繁
app.include_router(templates.router)  # 应该放在最上边，使用最频繁
app.include_router(dependencies.router)  # 应该放在最上边，使用最频繁
app.include_router(file.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)

models.Base.metadata.create_all(engine)


# @app.get('/')
# def index():
#     return "Hello World!"


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={'detail': exc.name}
    )


@app.get("/")
async def get():
    return HTMLResponse(html)


clients = []


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


# m2 start
# m1 start
# m1 end
# m2 end
@app.middleware("http")
async def add_middleware1(request: Request, call_next):
    start_time = time.time()
    print('m1 start')
    response = await call_next(request)
    print('m1 end')
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response


@app.middleware("http")
async def add_middleware2(request: Request, call_next):
    start_time = time.time()
    print('m2 start')
    response = await call_next(request)
    print('m2 end')
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response


@app.exception_handler(HTTPException)
def custom_handler(request: Request, exc: HTTPException):
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/files', StaticFiles(directory="files"), name='files')
app.mount('/templates/static', StaticFiles(directory="templates/static"), name="static")
