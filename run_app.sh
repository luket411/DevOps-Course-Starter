docker run \
    -it \
    -P \
    --network host \
    --env http_proxy="http://localhost:3128" \
    --env https_proxy="http://localhost:3128" \
    --env-file .env \
    todo-app