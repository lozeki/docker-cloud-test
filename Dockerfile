FROM ubuntu:xenial

COPY . /src

WORKDIR /src

RUN apt-get update
RUN	apt-get install -y talk
RUN apt-get install -y python3-pip
RUN apt-get install -y python3 
