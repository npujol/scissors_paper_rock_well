FROM python:3.9.2-slim-buster
ARG CURRENT_ENV=local

ENV CURRENT_ENV=${CURRENT_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 

WORKDIR /code  
COPY poetry.lock pyproject.toml /code/

RUN pip install poetry


RUN poetry config virtualenvs.create false \
  && poetry install $(test $CURRENT_ENV = production && echo "--no-dev") --no-interaction --no-ansi

COPY ./ /code/

CMD gunicorn -w 4 -k uvicorn.workers.UvicornH11Worker scissors_paper_rock_well.api:app -b 0.0.0.0:8000