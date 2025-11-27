FROM python:3.12-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt* pyproject.toml* ./

# Install dependencies
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    elif [ -f pyproject.toml ]; then \
        pip install --no-cache-dir .; \
    fi

# Copy the rest of the application
COPY . .

# Generate the static site
RUN pelican content -s publishconf.py

# Serve the static files
CMD ["python", "-m", "http.server", "8000", "--directory", "output"]
