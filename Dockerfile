FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Mattholy <smile.used@hotmail.com>"

WORKDIR /app/app

ENV ACCESS_LOG=/app/data/logs/access_log.log \
    ERROR_LOG=/app/data/logs/error_log.log

COPY ./kryta_server /app

ADD ./requirements.txt /app/app/requirements.txt
ADD ./kryta_server/prestart.sh /app/prestart.sh