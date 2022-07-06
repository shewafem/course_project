from django.db import models
from event.models import Event

class Ticket(models.Model):
    name = models.CharField(verbose_name='Название билета', max_length=255)
    cost = models.IntegerField(verbose_name="Цена билета")
    advanced = models.BooleanField(verbose_name="Привилегированный")
    seat = models.CharField(verbose_name="Место", max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="tickets/photos")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Билет'
        verbose_name_plural = 'Билеты'