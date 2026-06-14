FROM python:3.12-alpine3.24

# Set the working directory to /srv in the container
WORKDIR /srv

# Copy source files to the container
COPY ./src/ ./src/

ENTRYPOINT ["python", "src/app.py"]
