
FROM python:3.9.7

LABEL maintainer="lance.vanduin@student.uva.nl"

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR app

ENV FLASK_APP=main.py

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]