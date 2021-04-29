from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


CHOICES = (
        ('Conferences', 'Conferences'),
        ('Workshops and classes','Workshops and classes'),
        ('Awards and competitions', 'Awards and competitions'),
        ('Festivals and parties', 'Festivals and parties'),
        ('Birthday', 'Birthday'),
    )

class Event(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    detail = models.TextField(max_length=2000)
    event_type = models.CharField(max_length=100, choices=CHOICES)
    event_logo = models.FileField()
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)

    def get_absolute_url(self):
        return reverse('Event:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
