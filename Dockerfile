FROM python:3.10

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install poetry

# Do not create a virtual environment since container has single app
RUN poetry config virtualenvs.create false

COPY src/ pyproject.toml poetry.toml poetry.lock .

RUN poetry install --no-interaction

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]