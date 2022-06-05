FROM python:3.10.4-slim-bullseye
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN python3 -m venv .
RUN python3 -m pip install pip==22.1.2
RUN python3 -m pip install setuptools==62.3.2
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY ./app /app
EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "server:app"]
