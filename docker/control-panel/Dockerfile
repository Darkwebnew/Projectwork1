# Use official Python runtime as the base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Render dynamic port (defaults to 8000 for local use)
ENV PORT=8000

# Run the FastAPI server
CMD ["python", "run_server.py"]
