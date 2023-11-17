#!/bin/bash

docker build -t naralabs .

docker run -p 8000:8000 -p 27017:27017 naralabs