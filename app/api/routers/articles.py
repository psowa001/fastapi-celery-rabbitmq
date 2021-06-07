from fastapi import APIRouter
from fastapi import FastAPI, status
from typing import List, Any

from schemas import Article, ArticleCreate, ArticleUpdate
from worker import insert_article, delete_article, update_article
from db import get_all_articles, get_article_by_id
from models import articles

router = APIRouter()

@router.post("/", status_code = status.HTTP_200_OK)
def create_article(article: ArticleCreate) -> Any:
    insert_article.delay(dict(article))
    return {"details": "Article created."}

@router.get("/", status_code = status.HTTP_200_OK)
async def all_articles() -> List[Article]:
        return await get_all_articles()

@router.put("/{article_id}/", status_code = status.HTTP_200_OK)
async def update_article_details(article_id: int, article: ArticleUpdate) -> Any:
    update_article.delay(article_id=article_id, article_dict=dict(article))
    return {"details": "Article updated."}

@router.get("/{article_id}/", status_code = status.HTTP_200_OK)
async def article_by_id(article_id: int) -> Article:
    return await get_article_by_id(article_id)

@router.delete("/{article_id}", status_code=status.HTTP_200_OK)
async def delete_article_by_id(article_id: int) -> Any:
    delete_article.delay(article_id=article_id)
    return {"detail": "Article deleted."}