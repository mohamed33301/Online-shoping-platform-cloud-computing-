# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install build essentials and PostgreSQL development files
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    libpq-dev \
    && apt-get clean

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Flask application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
