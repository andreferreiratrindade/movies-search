FROM mcr.microsoft.com/devcontainers/python:3.11

# Set the working directory inside the container
WORKDIR /workspace

# Install system dependencies if needed (ChromaDB sometimes requires sqlite3 updates)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# [Optional] Set environment variables
ENV PYTHONUNBUFFERED=1
