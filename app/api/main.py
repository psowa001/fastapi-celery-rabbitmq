from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db import metadata, engine, database
from api.routers import articles
import models

metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI, Celery, BabbitMQ application")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles.router, prefix="/articles", tags=["articles"])