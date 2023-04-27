# CSC 488 Midterm Assignment analyzing International Space Station Data

Within this folder contains a python script, dockerfile, pytests, ISS sighting and position xml data, and a Makefile for automation purposes. Within terminal write "make startUp" doing so will first pull a Redis version 6 image from docker, start a redis container on port 5001 and execute Dockerfile and execute python script. "make shutdown" command is used to stop the redis container. "make pytest" command is used to execute pytest related to python script.

ISS sighting and positional data retrieved from:
https://data.nasa.gov/Space-Science/