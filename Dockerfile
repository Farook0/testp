# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 4000

# Run the application
CMD ["python", "app.py"]
