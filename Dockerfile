FROM python:3.10-buster

ENV production=True
ENV DJANGO_SETTINGS_MODULE=smitable.settings.prod
WORKDIR /app
COPY ./requirements.txt /app/
RUN python3 -m pip install -r requirements.txt
COPY . /app/
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
#RUN python3 manage.py loaddata fixtures/initial_data.json
EXPOSE 8000
CMD ["gunicorn", "smitable.wsgi:application", "reload", "--bind","0.0.0.0:8000"]
