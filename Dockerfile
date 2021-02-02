FROM python:3.8.0-slim-buster

ADD requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]