FROM python:3.9.7-slim-bullseye
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN python3 -m venv .
RUN python3 -m pip install pip==21.3.1
RUN python3 -m pip install setuptools==58.5.3
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY ./app /app
EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "server:app"]
