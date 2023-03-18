# Generated by Django 4.1.7 on 2023-03-14 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
        ('ks_students', '0011_remove_profile_user_alter_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='mentor.profile'),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(choices=[('ChuvSU', 'ЧГУ им. И.Н. Ульянова'), ('politech', 'Московский политех'), ('other', 'Прочее')], max_length=200, verbose_name='Место учебы'),
        ),
    ]