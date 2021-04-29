from celery import Celery
from django.core import mail

app = Celery()
@app.task
def send_email(email, message):
    emails = (
    (message, 'temp1451@gmail.com', [email]),
    )
    results = mail.send_mass_mail(emails)