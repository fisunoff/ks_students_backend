# Generated by Django 4.1.7 on 2023-03-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ks_students', '0014_alter_student_admission_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото профиля'),
        ),
    ]