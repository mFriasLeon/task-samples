FROM python:3.8.3-slim-buster

# Set the working directory to /app
WORKDIR /workspace

RUN apt-get update

RUN apt-get install -y python3

RUN apt update && apt install python3-pip -y

# Install MongoDB
RUN apt-get update && apt-get install -y gnupg wget
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt-get update && apt-get install -y mongodb-org

# Copy the current directory contents into the container at /app
COPY . /workspace

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Create the MongoDB data directory
RUN mkdir -p /data/db


# Expose ports
EXPOSE 8000
EXPOSE 27017

# Start MongoDB and uvicorn
CMD mongod & uvicorn main:app --host 0.0.0.0 --port 8000

