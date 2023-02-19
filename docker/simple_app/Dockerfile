# if this a huge string. use AS
FROM python AS base

#  env variables that will be available when docker is created.
ENV NEWVAR=10
ENV SLEEPTIME=2

# from local host will be copied to docker container
COPY . .

# After image creation, RUN command is used to run the commands inside container.
# During image build only, they are run.
RUN apt-get update

# At the start of the container, CMD is run. eg: service httpd start
# This is run every time unlike RUN.
# If the command is provided to > docker run, CMD will be skipped.
# CMD ["executable", "param1", "param2"]
CMD ["python3", "test_file.py"]


# same as CMD. But CMD will not run of docker run has parameter, but ENTRYPOINT will append parameter if docker run is provided.
# ENTRYPOINT ["executable", "param1", "param2"]
ENTRYPOINT ["python3", "test_file.py"]



# TO BUILD
# > docker build -t myapp .

# TO RUN
# > docker run myapp

# TO IGNORE CMD
# > docker run myapp python3 test_file.py

# ENTRPOINT append to docker run.
# ENTRYPOINT ["echo", "newhello"]
# docker run myapp "newworld" # newhello newworld


# If there are multiple entry points, only last will be executed.



