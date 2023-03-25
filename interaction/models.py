import datetime

from django.db import models
from django.utils import timezone
from tags.models import Tag


class Interaction(models.Model):
    interaction_name = models.TextField("Название")
    description = models.TextField("Описание", blank=True, null=True)
    type = models.ForeignKey("InteractionType",
                             verbose_name="Тип взаимодействия", on_delete=models.SET_NULL, blank=True, null=True)
    mentor = models.ForeignKey("mentor.Profile", related_name="interactions_to_mentor",
                               verbose_name="Наставник", on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey("ks_students.Student", related_name="interactions_to_student",
                                verbose_name="Студент", on_delete=models.SET_NULL, blank=True, null=True)
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата последнего изменения", default=timezone.now)
    start_date = models.DateField("Дата начала", blank=True, null=True, default=datetime.date.today)
    end_date = models.DateField("Дата окончания", blank=True, null=True)
    status = models.ForeignKey("Status", related_name="interactions_to_status",
                               verbose_name="Статус", on_delete=models.SET_NULL, blank=True, null=True, default="Новый")
    tags = models.ManyToManyField(Tag, verbose_name="Технологии(теги)", related_name='interactions_by_tag',
                                  blank=True, null=True)
    file = models.FileField(verbose_name="Прикрепленный файл", blank=True, null=True, upload_to='media/')

    def get_file_name(self):
        if self.file:
            return self.file.name.split("/")[-1]
        else:
            return None

    def __str__(self):
        return self.interaction_name

    class Meta:
        verbose_name = "Взаимодействие"
        verbose_name_plural = "Взаимодействия"
        ordering = ['status', 'start_date', 'end_date']


class InteractionType(models.Model):
    type_name = models.CharField("Название типа взаимодействия", max_length=50)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Тип взаимодействия"
        verbose_name_plural = "Типы взаимодействия"


class Status(models.Model):
    status_name = models.CharField("Название статуса", max_length=50)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
