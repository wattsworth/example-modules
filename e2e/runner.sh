#!/bin/bash

docker-compose up --abort-on-container-exit --build
docker-compose rm -f
