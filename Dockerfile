# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the port on which the Flask app is running
EXPOSE 5000

# Set the entry point for the container
ENTRYPOINT ["python", "app.py"]
