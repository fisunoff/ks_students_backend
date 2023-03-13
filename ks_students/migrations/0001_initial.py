# Generated by Django 4.1.7 on 2023-03-13 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('university', models.CharField(max_length=200, verbose_name='Место учебы')),
                ('admission_year', models.IntegerField(verbose_name='Год поступления')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=50, verbose_name='e-mail')),
                ('communication_other', models.CharField(max_length=200, verbose_name='Другие способы коммуникации')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания учетной записи')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(null=True)),
                ('position', models.TextField(max_length=200, verbose_name='Должность')),
                ('mentor', models.BooleanField(verbose_name='Является наставником')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(verbose_name='Тип взаимодействия')),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('time_edit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего изменения')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('status', models.CharField(default='new', max_length=50, verbose_name='Статус')),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ks_students.profile')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ks_students.student')),
            ],
        ),
    ]