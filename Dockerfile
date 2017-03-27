FROM ubuntu:xenial

COPY . /src

WORKDIR /src

RUN apt-get update

RUN apt-get install python3.6 
