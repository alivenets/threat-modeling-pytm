FROM python:3.8.6-alpine

RUN apk update
RUN apk add graphviz python3 ttf-freefont
RUN pip3 install pytm

ENTRYPOINT /bin/sh