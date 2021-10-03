FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="Mattholy <smile.used@hotmail.com>"

# ENV ACCESS_LOG=/app/logs/access_log.log \
#     ERROR_LOG=/app/logs/error_log.log

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./app/pyproject.toml ./app/poetry.lock* /app/

RUN poetry install --no-root --no-dev \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./app /app
