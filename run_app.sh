alias prod="docker run -d -p 5800:8000 --env-file .env todo-app:prod"
alias prod_with_cli="docker run -it -p 5800:8000 --env-file .env todo-app:prod"
alias dev='docker run -it -p 5800:5000 --env-file .env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev'
alias testing="docker run -it --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:test"

# These files are being kept as I haven't set up docker compose to work properly with the office proxy. So it's useful to still have these additionally