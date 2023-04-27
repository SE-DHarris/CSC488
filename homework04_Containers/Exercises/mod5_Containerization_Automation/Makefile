# 1. Builds your Docker image in your name space
# 2. Runs a test command or test script to confirm your image is working
# 3. Pushes your image to Docker Hub

NAME ?= Dontel

all: build run push

images:
    docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

build:
	docker build -t ${NAME}/ml_data_analysis:1.0 .

run:
	docker run --rm -v \${PWD}:/data ${NAME}/ml_data_analysis:1.0 ml_data_analysis.py/data/Meteorite_Landings.json

push:
	docker push ${NAME}/ml_data_analysis:1.0