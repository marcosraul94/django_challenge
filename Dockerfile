FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

# install postgres dependencies
RUN apk update \
 && apk add postgresql-dev gcc python3-dev musl-dev
 
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app
