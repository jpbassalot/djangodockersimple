FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY app/ /app
RUN cd /app && pipenv install --system

# Create and switch to a new user
RUN useradd --create-home appuser
USER appuser

WORKDIR /app
