FROM python:3.9-buster 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]