FROM tiangolo/uwsgi-nginx-flask:python3.8

LABEL maintainer="Mattholy <smile.used@hotmail.com>"

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
&& apt clean \
&& apt update \
&& echo 'Asia/Shanghai' >/etc/timezone

COPY ./app /app
