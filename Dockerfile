FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app


RUN pip install --upgrade pip
RUN pip install poetry


COPY pyproject.toml poetry.lock* ./

RUN poetry install  --without dev --no-interaction --no-root

COPY src ./src/


CMD ["python3", "src.main.py"]