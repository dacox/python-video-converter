FROM python:2.7-stretch

RUN apt-get update \
    && apt-get install -y ffmpeg

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
