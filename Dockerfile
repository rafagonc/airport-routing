FROM python:3.6-alpine3.9

COPY requirements.txt /app/requirements.txt
RUN pip install --requirement /app/requirements.txt

COPY . /app
WORKDIR /app
USER root

CMD ["python", "manage.py"]