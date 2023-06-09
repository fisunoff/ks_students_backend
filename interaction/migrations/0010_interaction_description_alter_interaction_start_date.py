# Generated by Django 4.1.7 on 2023-03-19 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0009_alter_interaction_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 3, 19), null=True, verbose_name='Дата начала'),
        ),
    ]
