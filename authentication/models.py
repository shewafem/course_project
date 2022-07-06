from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#from ticket.models import Ticket
from authentication.managers import UserManager



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, verbose_name='Email-адрес', unique=True)
    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    photo = models.ImageField(verbose_name="Фото", upload_to='users/photos')
    is_active = models.BooleanField(default=False, verbose_name='Активирован')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False, verbose_name='Админ')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname',]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name= 'Пользователь'
        verbose_name_plural = 'Пользователи'