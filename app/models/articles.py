from sqlalchemy import Table, Column, Integer, String, DateTime

from db import metadata

articles = Table(
    'articles', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('description', String),
    Column('content', String)
)