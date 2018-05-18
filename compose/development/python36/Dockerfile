FROM python:3.6-stretch

RUN apt update \
    && apt install -y ffmpeg

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
