FROM python:3.8-slim-buster

WORKDIR /app/flask

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]