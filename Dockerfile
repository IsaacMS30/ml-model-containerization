# Use the slim python image
FROM python:3.11-slim

# Working directory inside the container
WORKDIR /code

# Copy requirements file
COPY ./requirements.txt /code/requirements.txt

# Install all requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code into container
COPY ./app /code/app

# Expose port 8080
EXPOSE 8000

# Command to execute API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]