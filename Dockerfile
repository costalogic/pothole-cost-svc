# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run api.py when the container launches
COPY . .
CMD ["python", "api.py"]