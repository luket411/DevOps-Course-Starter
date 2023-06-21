#!/bin/bash
echo "building prod ..."
docker build --target production --tag todo-app:prod .
echo "building dev ..."
docker build --target development --tag todo-app:dev .
echo "building tests ..."
docker build --target testing --tag todo-app:test .

# These files are being kept as I haven't set up docker compose to work properly with the office proxy. So it's useful to still have these additionally