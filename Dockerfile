# Use official Python image as the base image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the pyproject.toml and poetry.lock files to the working directory
COPY pyproject.toml poetry.lock* /usr/src/app/

# Install Poetry
RUN pip install poetry

# Install the dependencies in the Docker container
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the working directory
COPY . .

# Make Scripts Executable
RUN chmod +x ./scripts/run.sh

# Expose the port the app runs on
EXPOSE 5000

# Run Entrypoint
CMD ./scripts/run.sh app
