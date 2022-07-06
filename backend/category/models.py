from django.db import models
from event.models import Event

class Category(models.Model):
    
    name = models.CharField(verbose_name="Название категории", max_length=255)
    description = models.TextField(verbose_name="Описание")
    events = models.ManyToManyField(verbose_name='Мероприятия', to=Event, related_name='categories')
    photo = models.ImageField(verbose_name='Фото', upload_to='categories/photos')
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural = 'Категории'