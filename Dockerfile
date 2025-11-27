FROM python:3.12-slim

WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies (including pelican and any other dependencies from pyproject.toml)
RUN pip install --no-cache-dir .

# Copy the rest of the application
COPY . .

# Generate the static site
RUN pelican content -s publishconf.py

# Serve the static files on port 3000 (Coolify's default)
EXPOSE 3000
CMD ["python", "-m", "http.server", "3000", "--directory", "output"]
