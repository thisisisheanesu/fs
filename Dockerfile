FROM python:3.11.6

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8045

CMD ["python", "manage.py", "runserver", "0.0.0.0:8045"]