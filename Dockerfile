# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local Python script (and any other dependencies) into the container
COPY producer.py /app/producer.py

RUN pip install confluent-kafka

# Command to run the Python script
CMD tail -f /dev/null