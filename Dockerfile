FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Mattholy <smile.used@hotmail.com>"

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
&& echo 'Asia/Shanghai' >/etc/timezone

COPY ./app /app
