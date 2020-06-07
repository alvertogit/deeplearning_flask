FROM python:3.7.7-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN python -m venv .
RUN pip install pip==20.1.1
RUN pip install setuptools==47.1.1
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app
EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "server:app"]
