from django.db import models

class Location(models.Model):

    name = models.CharField(verbose_name="Название места", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    address = models.TextField(verbose_name="Адрес")
    photo = models.ImageField(verbose_name="Фото", upload_to='locations/photos')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Место проведения'
        verbose_name_plural = 'Места проведения'