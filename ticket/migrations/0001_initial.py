# Generated by Django 4.0.6 on 2022-07-06 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название билета')),
                ('cost', models.IntegerField(verbose_name='Цена билета')),
                ('advanced', models.BooleanField(verbose_name='Привилегированный')),
                ('seat', models.CharField(max_length=255, verbose_name='Место')),
                ('photo', models.ImageField(upload_to='tickets/photos')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
    ]
