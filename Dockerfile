FROM python:3.9.2-slim-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 
  
COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install

COPY ./scissors_paper_rock_well ./scissors_paper_rock_well

CMD uvicorn scissors_paper_rock_well.api:app 