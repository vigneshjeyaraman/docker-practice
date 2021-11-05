FROM python

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN pip install psycopg2

COPY . /app/

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]