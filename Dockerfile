ARG BASE_IMAGE=python:3.12.0a7-buster
ARG START_POINT=${BASE_IMAGE}

# if "base_with_proxy" is passed as build arg, then proxy vars get exported for the image, else they dont.
FROM ${BASE_IMAGE} as base_with_proxy

ENV http_proxy="http://172.17.0.1:3128"
ENV https_proxy="http://172.17.0.1:3128"

FROM ${START_POINT} as base

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

# Make workspace
WORKDIR /app
COPY poetry.toml pyproject.toml ./

# Install poetry dependencies
RUN poetry install --only main

FROM base as production

# Copy production files
COPY todo_app /app/todo_app

# Set is_prod variable to make sure system gets run accordingly
ENV IS_PROD=1
EXPOSE 8000

# Sets gunicorn command to run
CMD poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as full_install

# Install development packages
RUN poetry install

FROM full_install as development

EXPOSE 5000
CMD poetry run flask run --host 0.0.0.0

FROM full_install as testing

# Copy unit tests to image
COPY tests /app/tests
COPY .env.test .

# Run unit tests
CMD poetry run pytest tests/

FROM full_install as e2e_testing

# Installs google chrome to image
RUN apt-get update && apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 fonts-liberation
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb

# Installs chrome driver to image
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d .

# Copy e2e tests
COPY e2e_tests /app/e2e_tests

# Simulate a production environment
ENV IS_PROD=1

# Run e2e tests
CMD poetry run pytest e2e_tests