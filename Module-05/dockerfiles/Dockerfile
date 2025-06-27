FROM quay.io/jupyter/tensorflow-notebook:hub-5.3.0

USER root
RUN apt update -y && apt install -y \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*

USER jovyan
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt