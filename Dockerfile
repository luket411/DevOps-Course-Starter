FROM python:3.12.0a7-buster

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
RUN export PATH="/root/.local/bin:$PATH"

WORKDIR /app
