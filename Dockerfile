# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

LABEL maintainer="dmurphy6@uoregon.edu"
RUN apt-get update -y

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary packages
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable & enable live reload
ENV FLASK_APP=app.py
ENV FLASK_ENV=development 

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
