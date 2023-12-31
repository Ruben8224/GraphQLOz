FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /numeros
WORKDIR /comics
COPY requirements.txt /numeros/
RUN pip install -r requirements.txt
COPY . /numeros/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080
