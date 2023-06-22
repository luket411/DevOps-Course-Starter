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

FROM testing as e2e_testing

RUN apt-get update && apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 fonts-liberation
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d .

COPY e2e_tests /app/e2e_tests

CMD poetry run pytest e2e_tests