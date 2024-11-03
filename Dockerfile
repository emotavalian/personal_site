FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code1

COPY requirements.txt /code1/
RUN pip install -r requirements.txt

COPY . /code1/