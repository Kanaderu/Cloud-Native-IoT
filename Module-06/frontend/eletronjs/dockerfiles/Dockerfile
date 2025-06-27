FROM node:lts-bookworm

# install electron dependencies
RUN apt-get update -y && \
    apt-get install -y \
        libnspr4-dev \
        libnss3-dev \
        libdbus-1-dev \
        libatk1.0-dev \
        libatk-bridge2.0-dev \
        libcups2-dev \
        libgtk-3-dev \
        libasound2-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD yarn run start