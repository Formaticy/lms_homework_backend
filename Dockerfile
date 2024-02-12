FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver ${BACKEND_HOST}:${BACKEND_PORT_CONTAINER}
