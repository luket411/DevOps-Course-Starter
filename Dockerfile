FROM python:3.12.0a7-buster as base

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

# Make workspace
WORKDIR /app
COPY poetry.toml pyproject.toml ./

# Install poetry dependencies
RUN poetry install --only main

# Copy production files
FROM base as production

COPY todo_app /app/todo_app
ENV IS_PROD=1
EXPOSE 8000
CMD poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development

RUN poetry install

EXPOSE 5000
CMD poetry run flask run --host 0.0.0.0

FROM base as testing

RUN poetry install

COPY tests /app/tests
COPY .env.test .

CMD poetry run pytest tests/