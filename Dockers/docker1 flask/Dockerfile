FROM python:3.9-slim
COPY  . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD  ["python", "app.py"]