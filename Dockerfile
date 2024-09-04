# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port that the Django application will run on
EXPOSE 8000

# Set the environment variables
ENV DJANGO_SETTINGS_MODULE=library_project.settings

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]