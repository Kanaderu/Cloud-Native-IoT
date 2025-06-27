FROM python:3.13-bookworm

RUN apt-get update -y && \
    apt-get install -y \
        libmemcached-dev \
    && rm -rf /var/lib/apt/lists/*
COPY ./project /project
WORKDIR /project

RUN pip install -r requirements.txt