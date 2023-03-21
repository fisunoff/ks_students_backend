# Generated by Django 4.1.7 on 2023-03-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_options_alter_tag_unique_together'),
        ('interaction', '0012_interaction_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='tags',
            field=models.ManyToManyField(related_name='interactions_by_tag', to='tags.tag', verbose_name='Технологии(теги)'),
        ),
    ]