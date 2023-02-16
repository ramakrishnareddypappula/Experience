
# Use an official Python runtime as a parent image(base image)
FROM python:3.9-slim-buster

# Adds additional information to the image
# docker inspect myapp
LABEL version="1.0"
LABEL description="description of the image"
LABEL maintainer="maintainer email email@gmail.com"


# These are build time variables that can be used in other commands as shown below.
# > docker build --build-arg MYVERSION=10.1
# OR
ARG MYVERSION=10.1


# Set working directory for subsequent commands(RUN, CMD, ENTRYPOINT, COPY, ADD) to use.
# Creates if already not present.
WORKDIR /opt

# Copies test_file from current folder to /opt inside docker container.
COPY test_file.py ./


# Automatically extract tar, gzip etc from local and keep in container.
# Also Remote urls download.
# Automatically creates a directory if its not present.
# Recommand wget and curl commands to use instead of ADD.
ADD nohup.tar.gz ./


# Make 4000 tcp port available to the world outside this container.
# docker ps will have this port
EXPOSE 4000/tcp

RUN apt-get update

# Above ARG is used here.
RUN mkdir -p $MYVERSION
RUN apt install python3 -y
RUN apt install vim -y

ENTRYPOINT ["python3", "test_file.py"]


# TO BUILD
# > docker build -t myapp .

# To enter inside the docker comtainer.
# docker run -it --entrypoint bash myapp
# you will enter into /opt folder. test_file.py will be present.






