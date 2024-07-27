FROM python:3.12

EXPOSE 8080

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "/app/app.py"]