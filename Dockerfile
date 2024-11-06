FROM python:3.11-slim

WORKDIR /miac_task
COPY . /miac_task/

RUN pip install -r requirements.txt

CMD python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000
