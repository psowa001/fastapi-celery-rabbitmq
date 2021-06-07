from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Connection
from contextlib import contextmanager
import os
from databases import Database

postgres_host = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")
postgres_database = os.environ.get("POSTGRES_DB")
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(postgres_user, postgres_password, postgres_host, postgres_port, postgres_database)

engine = create_engine(DATABASE_URL)

metadata = MetaData()
database = Database(DATABASE_URL)

