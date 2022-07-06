# Generated by Django 4.0.6 on 2022-07-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='categories/photos', verbose_name='Фото')),
                ('events', models.ManyToManyField(related_name='categories', to='event.event', verbose_name='Мероприятия')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
