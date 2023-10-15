FROM python:3.9.11-slim-bullseye

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT 8000

WORKDIR /server/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/server/venv
ENV LOG_LEVEL "${LOG_LEVEL}"

# 1. Install env dependencies.
RUN apt-get update --fix-missing \
    && apt-get install -y gcc python3-pip python-dev build-essential git postgresql-client libpq-dev

# 2. Install python dependencies in a virtual env.
COPY ./requirements.txt /server/requirements.txt

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv "$VIRTUAL_ENV" \
    && pip install --upgrade --no-cache-dir pip \
    && pip --no-cache-dir install -r requirements.txt


COPY app /server/app

WORKDIR /server

CMD ["bash", "-c", "/server/venv/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port $PORT --log-level $LOG_LEVEL"]
