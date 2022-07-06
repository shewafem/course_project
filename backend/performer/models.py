from django.db import models

class Performer(models.Model):
    name = models.CharField(verbose_name="Выступающий", max_length=255)
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(verbose_name='Фото', upload_to='performers/photos')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Выступающий'
        verbose_name_plural = 'Выступающие'