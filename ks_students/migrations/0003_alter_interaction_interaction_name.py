# Generated by Django 4.1.7 on 2023-03-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ks_students', '0002_alter_interaction_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='interaction_name',
            field=models.TextField(verbose_name='Название'),
        ),
    ]