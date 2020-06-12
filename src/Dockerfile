# pull official base image
FROM python:3.8.3-slim-buster as builder
RUN pip install poetry
COPY poetry.lock pyproject.toml /build/

WORKDIR /build

# Remove without hashes after this is fixed: https://github.com/python-poetry/poetry/issues/1627
RUN poetry export --without-hashes -f requirements.txt > requirements.txt

# pull official base image
FROM python:3.8.1-alpine

COPY --from=builder /build/requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# add app
COPY . /usr/src/app