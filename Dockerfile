# ==========================
# Base Image
# ==========================
FROM python:3.12-slim

# ==========================
# Environment Variables
# ==========================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ==========================
# Working Directory
# ==========================
WORKDIR /app

# ==========================
# System Dependencies
# ==========================
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ==========================
# Install Python Dependencies
# ==========================
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==========================
# Copy Application
# ==========================
COPY . .

# ==========================
# Expose FastAPI Port
# ==========================
EXPOSE 8000

# ==========================
# Start Application
# ==========================
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]