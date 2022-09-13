FROM python:3.10.2-slim-buster

ENV LANG C.UTF-8

COPY entrypoint.sh entrypoint.sh

RUN pip install poetry==1.1.12

RUN poetry config virtualenvs.create false && \
    poetry config experimental.new-installer false && \
    poetry config installer.parallel false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY src src
ENV PYTHONPATH "${PYTHONPATH}:/src/"
COPY scripts scripts


EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
