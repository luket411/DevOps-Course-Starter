# Manual Dependencies

## Introduction

This project uses docker to automate dependency and package management. However if you want to run these steps manually, you can follow the steps layed out in this guide.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once all the dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:

```bash
poetry run flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running Tests

### Automatic testing

Once all the dependencies have been installed, automated tests can be ran with

```bash
poetry run pytest tests/
```

### E2E Testing

To run end to end tests that make changes to the Trello board, make sure you have your `.env` file setup and then run

```bash
poetry run pytest e2e_tests/
```

### Run linter

To run the python linter

```bash
poetry run autopep8 -r -i --max-line-length=200 --ignore-local-config .
```

### Run style checker

To run the style checker, run,

```bash
poetry run pycodestyle --max-line-length=200 --exclude=.venv,__pycache__,.pytest_cache .
```
