# Stage 1: Build & test
FROM python:3.11-slim as builder

WORKDIR /app
COPY app/ app/
COPY tests/ tests/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pytest --maxfail=1 --disable-warnings -q

# Stage 2: Production image
FROM python:3.11-slim
WORKDIR /app
COPY app/ app/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
