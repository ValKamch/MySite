FROM python:3-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/


#RUN pip install poetry && poetry install --no-root --no-directory

RUN pip install poetry

RUN poetry config virtualenvs.create false --local

RUN poetry install --no-dev

COPY . .





