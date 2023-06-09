alias prod="docker run -d -p 5800:8000 --env-file .env todo-app:prod"
alias prod_with_cli="docker run -it -p 5800:8000 --env-file .env todo-app:prod"
alias dev='docker run -it -p 5800:5000 --env-file .env --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev'
alias run_test="docker run -it --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:test"
