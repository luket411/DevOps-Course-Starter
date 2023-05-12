FROM python:3.12.0a7-buster

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN export PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY todo_app/*.py todo_app/
COPY todo_app/data/*.py todo_app/data/
COPY todo_app/templates/*.html todo_app/templates/
COPY .env.template .env
COPY poetry.toml .
COPY pyproject.toml .

