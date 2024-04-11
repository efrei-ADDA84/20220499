FROM python:3.11-alpine

WORKDIR /app

COPY tp1devopps.py .

RUN apk update && apk upgrade

RUN pip install --no-cache-dir requests==2.31.0

CMD ["python", "tp1devopps.py"]