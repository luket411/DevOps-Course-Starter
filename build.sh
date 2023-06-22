#!/bin/bash
if [[ -n "$1" ]]; then
    echo "building base ..."
    docker build --no-cache --tag todo-app .
    echo "===================================="
fi


echo "building prod ..."
docker build --target production --tag todo-app:prod .
echo "===================================="
echo "building dev ..."
docker build --target development --tag todo-app:dev .
echo "===================================="
echo "building tests ..."
docker build --target testing --tag todo-app:test .
echo "===================================="
echo "building e2e tests ..."
docker build --target e2e_testing --tag todo-app:e2e_test .

# These files are being kept as I haven't set up docker compose to work properly with the office proxy. So it's useful to still have these additionally