FROM python:3.9-slim

WORKDIR /app

COPY tp1devopps.py .


CMD ["python", "tp1devopps.py"]
