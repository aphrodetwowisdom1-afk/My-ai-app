# Dockerfile for AI Video Generation Application

# Use the official NVIDIA CUDA base image with Python 3.10
FROM nvidia/cuda:11.6.0-cudnn8-runtime-ubuntu20.04

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required dependencies
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["python3", "your_script.py"]