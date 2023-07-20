FROM python:3.10-buster

ENV production=True

WORKDIR /app
COPY ./requirements.txt /app/
RUN python3 -m pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["gunicorn", "smitable.wsgi:application", "reload", "--bind","0.0.0.0:8000"]
