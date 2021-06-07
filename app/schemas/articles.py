from typing import Optional
from datetime import datetime
from pydantic import BaseModel
import pickle

class ArticleBase(BaseModel):
    title: str
    description: str
    content: str

class ArticleCreate(ArticleBase):
    def __iter__(self):
        return iter(self.__dict__.items())

class ArticleUpdate(ArticleBase):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None

    def __iter__(self):
        return iter(self.__dict__.items())

class Article(ArticleBase):
    id: int