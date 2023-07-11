# Docker architecture

The table below explains the different docker compose services able to run

Service | Purpose | Needs `.env` | Port forwarded? | Contains app code? | Contains test code? | Contains e2e test code? | Command run
--- |---|---|---|---|---|---|---
`base` | Common steps all modes go through | N/a | N/a | No | No | No | N/a
`production` | Running the app with a production ready server | Yes | Yes | Copied | No | No | `poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"`
`development` | purpose | Yes | Yes | Mounted | No | No | `poetry run flask run --host 0.0.0.0`
`testing` | purpose | No | No | Mounted | Copied | No | `poetry run pytest tests`
`e2e_testing` | purpose | Yes | No | Mounted | No | Copied | `poetry run pytest e2e_tests`
`linter` | purpose | No | No | Mounted | Mounted | Mounted | `poetry run autopep8 -r -i --max-line-length=200 --ignore-local-config .`
`check_style` | purpose | No | No | Mounted | Mounted | Mounted | `poetry run pycodestyle --max-line-length=200 todo_app tests e2e_tests`
