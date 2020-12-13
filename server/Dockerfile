FROM python:3.8-slim-buster

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements.txt /server/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./server /server

EXPOSE 8000