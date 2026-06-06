FROM python:3.14-slim

WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies (including pelican and any other dependencies from pyproject.toml)
RUN pip install --no-cache-dir .

# Copy the rest of the application
COPY . .

# Generate the static site
RUN pelican content -s publishconf.py

# Create a non-root user and give it ownership of the app
RUN adduser --disabled-password --gecos "" appuser
RUN chown -R appuser:appuser /app
USER appuser

# Serve the static files on port 8080, listening on all interfaces
EXPOSE 8080
CMD ["python", "-m", "http.server", "8080", "--bind", "0.0.0.0", "--directory", "output"]
