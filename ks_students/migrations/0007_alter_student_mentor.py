# Generated by Django 4.1.7 on 2023-03-13 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ks_students', '0006_student_bio_student_mentor_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ks_students.profile'),
        ),
    ]
