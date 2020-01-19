FROM python:3.7.6-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN python -m venv .
RUN pip install pip==19.3.1
RUN pip install setuptools==45.1.0
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app
EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "server:app"]
