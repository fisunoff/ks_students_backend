# Generated by Django 4.1.7 on 2023-03-14 07:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentor', '0001_initial'),
        ('ks_students', '0011_remove_profile_user_alter_student_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.TextField(verbose_name='Название типа взаимодействия')),
            ],
            options={
                'verbose_name': 'Тип взаимодействия',
                'verbose_name_plural': 'Типы взаимодействия',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.TextField(verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_name', models.TextField(verbose_name='Название')),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('time_edit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего изменения')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mentor.profile', verbose_name='Наставник')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interaction.status', verbose_name='Статус')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ks_students.student', verbose_name='Студент')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interaction.interactiontype', verbose_name='Тип взаимодействия')),
            ],
            options={
                'verbose_name': 'Взаимодействие',
                'verbose_name_plural': 'Взаимодействия',
            },
        ),
    ]
