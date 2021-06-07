FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH = ./app
WORKDIR /app/

COPY /worker/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY /worker/ /app/worker/
COPY /db/ /app/db/
COPY /models/ /app/models/
COPY /schemas/ /app/schemas/
COPY __init__.py /app/