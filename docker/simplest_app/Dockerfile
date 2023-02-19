FROM ubuntu

CMD sleep 5

#OR
# CMD ["sleep", "5"]


# docker build -t myubuntu .
# docker build -t  name:tag foldername # -t is used to specify name.
# docker run myubuntu

# we can override sleep 5 with 10 sec using.
# docker run myubuntu sleep 10


# OR
FROM ubuntu
ENTRYPOINT  ["sleep"]

# docker run myubuntu 10


# OR
FROM ubuntu

ENTRYPOINT  ["sleep"]
CMD ["5"]
# only as list. not ENTRYPOINT  sleep CMD 5
# docker run myubuntu


# OR
FROM ubuntu

# docker build -t myubuntu .
# docker run --entrypoint sleep myubuntu 10



# example
# docker run -d --entrypoint sleep ubuntu 1000
# to run container in detached mode with sleep of 1000.


