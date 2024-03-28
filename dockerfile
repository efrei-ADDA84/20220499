FROM python:3.9-slim

WORKDIR /app

COPY tp1devopps.py .

RUN pip install requests

CMD ["python", "tp1devopps.py"]
