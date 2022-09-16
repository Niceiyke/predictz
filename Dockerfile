FROM python:3.10

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


RUN mkdir /app
RUN mkdir app/staticfiles
COPY ./app /app
WORKDIR /app

