from datetime import date
from django.db import models
from performer.models import Performer
from location.models import Location

class Event(models.Model):
    name = models.CharField(verbose_name="Название мероприятия", max_length=255)
    start = models.TimeField(verbose_name="Начало")
    end = models.TimeField(verbose_name="Конец")
    date = models.DateField(verbose_name="Дата проведения")
    description = models.TextField(verbose_name="Описание")
    #tickets = 
    location = models.ManyToManyField(verbose_name="Место проведения",to=Location, related_name='events')
    performer = models.ManyToManyField(verbose_name="Выступающий", to=Performer, related_name='events')
    photo = models.ImageField(verbose_name="Фото", upload_to='events/photos')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Мероприятие'
        verbose_name_plural = 'Мероприятия'