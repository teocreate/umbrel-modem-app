
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y gammu gammu-smsd

# Copy the app
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install flask

# Expose the port and run the app
EXPOSE 5000
CMD ["python", "app.py"]
