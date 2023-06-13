FROM python:3

RUN apt-get update && apt-get install -y python3

RUN pip install django

COPY . .
RUN python manage.py migrate

CMD ["python", "manage.py" "runserver", "0.0.0.0:8080"]
