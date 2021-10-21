FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Mattholy <smile.used@hotmail.com>"

# ENV ACCESS_LOG=/app/app/logs/access_log.log \
#     ERROR_LOG=/app/app/logs/error_log.log

COPY ./app /app

ADD ./requirements.txt /app/requirements.txt