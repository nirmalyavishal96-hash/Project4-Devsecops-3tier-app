# Use slimmer base image to reduces vulnerabilities
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies only required once during build time 
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]