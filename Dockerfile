FROM python:3.6.7-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /api
WORKDIR /api
COPY requirements.txt /api
RUN pip install -r requirements.txt
COPY ./api /api
EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "server:app"]