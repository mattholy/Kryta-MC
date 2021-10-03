FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Mattholy <smile.used@hotmail.com>"

# ENV ACCESS_LOG=/app/logs/access_log.log \
#     ERROR_LOG=/app/logs/error_log.log

ADD ./requirements.txt /app/requirements.txt

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -r requirements.txt

COPY ./app /app