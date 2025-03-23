# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY script.py /app/

# Make the script executable
RUN chmod +x /app/script.py

# Run the script when the container launches
CMD ["python", "/app/script.py"] 