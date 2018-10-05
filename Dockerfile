FROM python:3
ENV PYTHONUNBUFFERED 1

# Copying all the app code
# COPY . /app

# Install python requirements
COPY ./requirements /requirements
RUN pip install -U pip
RUN pip install -r /requirements/dev.txt

# Working directory
WORKDIR /app

ENV PYTHONPATH /app/apzm
