# Multi-stage build for production deployment
FROM node:18-alpine AS frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production

COPY frontend/ ./
RUN npm run build

# Python backend stage
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=blog_project.settings

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        musl-dev \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r backend/requirements.txt \
    && pip install gunicorn

# Copy Django project
COPY backend/ ./backend/

# Copy built frontend files
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Create staticfiles directory
RUN mkdir -p /app/backend/staticfiles

# Collect static files
WORKDIR /app/backend
RUN python manage.py collectstatic --noinput

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/stats/ || exit 1

# Run gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "blog_project.wsgi:application"]