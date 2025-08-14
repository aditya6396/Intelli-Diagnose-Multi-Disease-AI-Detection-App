# Use an official Python runtime as a parent image
FROM python:3.10.0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /home/cpatwadityasharma/AdityaBackup/medical

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in medical_req.txt
RUN pip install --no-cache-dir -r medical_req.txt

# Expose the port the app runs on
EXPOSE 8000

# Run wsgi.py when the container launches
CMD ["python", "./wsgi.py"]
