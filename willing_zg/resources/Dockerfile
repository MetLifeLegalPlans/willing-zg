FROM 818831340115.dkr.ecr.us-east-1.amazonaws.com/python:3.10

RUN pip install --upgrade pip poetry

RUN mkdir -p /code
WORKDIR /code

COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-dev

COPY . .

CMD poetry run ./manage.py wait_for_db && poetry run ./manage.py migrate && poetry run ./manage.py createcachetable && poetry run gunicorn -w 4 -b 0.0.0.0:3000 backend.asgi -k zygoat_django.uvicorn_worker.ZygoatUvicornWorker
