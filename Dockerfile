FROM python:3.12.0a7-buster as base

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

# Make workspace
WORKDIR /app
COPY poetry.toml .
COPY pyproject.toml .

# Install poetry dependencies
RUN poetry install

# Copy production files
FROM base as production

COPY todo_app/templates/layout.html todo_app/templates/
COPY todo_app/templates/prod_index.html todo_app/templates/index.html
COPY todo_app/*.py todo_app/
COPY todo_app/data/*.py todo_app/data/

EXPOSE 8000
CMD poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development

EXPOSE 5000
CMD poetry run flask run --host 0.0.0.0