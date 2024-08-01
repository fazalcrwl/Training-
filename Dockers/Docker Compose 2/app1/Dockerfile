FROM python:3.9-slim

WORKDIR /app

COPY database.py .

RUN pip install sqlite3

CMD ["python", "database.py"]
