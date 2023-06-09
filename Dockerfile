FROM python:3.12.0a7-buster

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

WORKDIR /app

COPY poetry.toml .
COPY pyproject.toml .
RUN poetry install

COPY todo_app/templates/*.html todo_app/templates/
COPY todo_app/*.py todo_app/
COPY todo_app/data/*.py todo_app/data/

CMD poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"