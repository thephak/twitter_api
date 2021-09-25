FROM python:3.9.7
RUN apt-get update
COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH="."
ENV PYTHONUNBUFFERED 1
EXPOSE 8080

RUN python ./app/server.py