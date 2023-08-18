# Use a base image that supports Python
FROM python:3.11.4-slim

# Creates the 'app' folder in the Docker image, where the project will be copied
RUN mkdir -p /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements/prod.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]