# Generated by Django 4.1.7 on 2023-03-18 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0007_alter_interaction_options_alter_interaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 3, 18), null=True, verbose_name='Дата начала'),
        ),
    ]
