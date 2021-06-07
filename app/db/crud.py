from typing import List

from models import articles
from schemas import Article
from db import database

async def get_article_by_id(article_id: int) -> Article:
    return await database.fetch_one(query=articles.select().where(articles.c.id == article_id))

async def get_all_articles() -> List[Article]:
    return await database.fetch_all(query=articles.select())