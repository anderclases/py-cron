FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl tzdata && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install schedule
