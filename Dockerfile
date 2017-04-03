FROM ubuntu:xenial

COPY . /src
WORKDIR /src
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils && apt-get install -y python3 python3-pip && apt-get -y upgrade
RUN pip3 install Werkzeug Jinja2 Flask
