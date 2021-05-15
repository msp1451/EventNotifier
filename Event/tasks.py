from celery import Celery
from django.core.mail import send_mail
from celery import shared_task

app = Celery()
@app.task
def send_email(email, message):
    emails = ('test mail', message, 'temp1451@gmail.com', [email])
    results = send_mail(*emails)

@shared_task
def add(x, y):
    return x+y
