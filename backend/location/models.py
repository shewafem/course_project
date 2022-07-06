from django.db import models
from event.models import Event

class Location(models.Model):

    name = models.CharField(verbose_name="Название места", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    address = models.TextField(verbose_name="Адрес")
    event = models.ManyToManyField(to=Event, related_name='locations')
    photo = models.ImageField(verbose_name="Фото", upload_to='locations/photos')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Место проведения'
        verbose_name_plural = 'Места проведения'