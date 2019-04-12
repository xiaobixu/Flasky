FROM jfloff/alpine-python:2.7-slim

COPY . /app
WORKDIR /app

RUN apk add --no-cache sqlite3
RUN pip install -r requirements.txt


ENV FLASK_PORT 8080
ENV FLASK_APP demo_app
CMD ["flask run"]
