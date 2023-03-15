# Generated by Django 4.1.7 on 2023-03-14 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
        ('ks_students', '0010_alter_profile_mentor_alter_profile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Наставник', to='mentor.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('name', 'surname', 'patronymic')},
        ),
        migrations.DeleteModel(
            name='Interaction',
        ),
        migrations.DeleteModel(
            name='InteractionType',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
