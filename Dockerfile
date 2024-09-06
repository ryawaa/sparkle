
# base layer
FROM python:3.12-alpine as base
# create a venv


ARG DEV=false

ENV VIRTUAL_ENV=/sparkle/.venv \
    PATH="/sparkle/.venv/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

RUN apk update && \
    apk add libpq

# builder layer
FROM base as builder
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \  
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR='/tmp/poetry_cache'

RUN apk update && \
    apk add musl-dev build-base gcc gfortran openblas-dev

WORKDIR /sparkle

RUN pip install poetry==1.8.3

# Install the app
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR; 

FROM base as runtime

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app ./app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

