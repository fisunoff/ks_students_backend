import datetime

from django.db import models
from django.utils import timezone


class Interaction(models.Model):
    interaction_name = models.TextField("Название")
    type = models.ForeignKey("InteractionType",
                             verbose_name="Тип взаимодействия", on_delete=models.SET_NULL, null=True)
    mentor = models.ForeignKey("mentor.Profile", related_name="interactions_to_mentor",
                               verbose_name="Наставник", on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey("ks_students.Student", related_name="interactions_to_student",
                                verbose_name="Студент", on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата последнего изменения", default=timezone.now)
    start_date = models.DateField("Дата начала", blank=True, null=True, default=datetime.date.today())
    end_date = models.DateField("Дата окончания", blank=True, null=True)
    status = models.ForeignKey("Status", related_name="interactions_to_status",
                               verbose_name="Статус", on_delete=models.SET_NULL, null=True, default="Новый")

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
