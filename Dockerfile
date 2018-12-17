FROM python:3.6.7-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /api
WORKDIR /api
COPY requirements.txt /api
RUN pip install --no-cache-dir -r requirements.txt
COPY ./api /api
EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "server:app"]
