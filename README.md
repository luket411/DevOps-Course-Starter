# DevOps Apprenticeship: Project Exercise

## System Requirements

### Docker installation

This project uses docker to manage the dependencies and packages needed to run the app.
To install docker follow the instructions on the docker website:

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

## Dependencies

### Setting up Trello

Before the app can be used a trello board must be setup with a "To Do" list and a "Done" list. The board ID must then be put in the [.env](./.env) file along with trello credentials.

### Setting up .env

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

In here is also where you should define the trello [BOARD_ID](./.env#L9) for your trello board and your [TRELLO_KEY](./.env#L11) and [TRELLO_TOKEN](./.env#L12) for your authentication.

## Running the app

This project uses a set of docker images for production and deployment versions of the app. These images can be built using the [Dockerfile](Dockerfile) in the repository which will manage the installation of all dependencies for the project.

To setup and run the app, use either the [production](#production) or [development](#development) commands and then visit [localhost:5800](http://localhost:5800).

### Production

To build and run the production version of the app, run the following command:

```bash
docker compose up production
```

The production version of the app includes the source codes as a part of the image therefore requires rebuilding everytime a change has made. However this also means the app can be exported more easily.

### Development

To build and run the development version of the app, run the following command:

```bash
docker compose up development
```

Unlike the production version, the development image does not contain source code and instead needs the [todo_app](./todo_app/) directory mounted to the container at run time. However this provides the benefit of not requiring the image to be rebuilt each time a change is made, making the speed of future development of the app much faster.

## Running Tests

Unit tests can also be ran with a similar docker target called "testing". The command to run these tests are:

```bash
docker compose up testing
```

## Running without Docker

If you want to run the app or tests without docker, follow the [manual_dependency guide](./manual_dependencies.md).
