 

.PHONEY: startUp
# Automate startup 
startUp: pull start build

# Build docker container
build: 
		docker build DockerFiles

# Pull Redis image
pull: 
		docker pull redis:6

# Start Redis server
start:
		docker run -d -p 6379:5001 --name=dontel-redis redis:6

# Shut down Redis server
shutdown:
		docker rm -f dontel-redis

# Run pytest
pytest:
		pytest test_ISS_midterm.py

