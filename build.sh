#!/bin/bash
echo "building prod ..."
docker build --target production --tag todo-app:prod .
echo "building dev ..."
docker build --target development --tag todo-app:dev .
