# Lightweight Python image.
FROM python:3.9-slim

# Working directory of the /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages.
RUN pip install --no-cache-dir -r requirements.txt

# Expose the required ports for FastAPI
EXPOSE 8000

# Uvicorn command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]