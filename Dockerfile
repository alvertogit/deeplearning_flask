FROM python:3.12-slim-bookworm
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
COPY pyproject.toml uv.lock README.md /app/
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv sync --no-dev --no-install-project
COPY ./app /app
EXPOSE 5000
CMD ["uv", "run", "gunicorn", "--bind", ":5000", "server:app"]
