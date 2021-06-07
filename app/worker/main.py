from celery import Celery
from celery.signals import worker_process_init, worker_process_shutdown
import datetime
import os
from sqlalchemy.engine import Connection

from models import articles
from db import engine
from schemas import ArticleCreate

rabbit_host = os.environ.get("RABBITMQ_HOST")
rabbit_user = os.environ.get("RABBITMQ_USER")
rabbit_password = os.environ.get("RABBITMQ_PASSWORD")

db_conn: Connection = None

@worker_process_init.connect
def init_worker(**kwargs):
    global db_conn
    print('Initializing database connection for worker.')
    db_conn = engine.connect()


@worker_process_shutdown.connect
def shutdown_worker(**kwargs):
    global db_conn
    if db_conn:
        print('Closing database connectionn for worker.')
        db_conn.close()

celery = Celery('celery', broker='amqp://{}:{}@{}'.format(rabbit_user, rabbit_password, rabbit_host))

@celery.task
def insert_article(article_dict: dict):
    db_conn.execute(articles.insert().values(article_dict))

@celery.task
def update_article(article_dict: dict, article_id: int):
    db_conn.execute(articles.update().where(articles.c.id == article_id).values({k: v for k, v in article_dict.items() if v}))

@celery.task
def delete_article(article_id: int):
    db_conn.execute(articles.delete().where(articles.c.id == article_id))