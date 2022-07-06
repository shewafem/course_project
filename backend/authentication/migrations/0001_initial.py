# Generated by Django 4.0.6 on 2022-07-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email-адрес')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('photo', models.ImageField(upload_to='users/photo', verbose_name='Фото')),
                ('is_active', models.BooleanField(default=False, verbose_name='')),
                ('is_staff', models.BooleanField(default=False, verbose_name='')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
