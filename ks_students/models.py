from django.db import models
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    UNIVERSITIES = (("ЧГУ им. И.Н. Ульянова", "ЧГУ им. И.Н. Ульянова"),
                    ("Московский политех", "Московский политех"),
                    ("Прочее", "Прочее"))

    name = models.CharField(verbose_name="Имя", max_length=50, blank=False)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, blank=False)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    university = models.CharField(verbose_name="Место учебы", max_length=200, choices=UNIVERSITIES, blank=True, null=True)
    admission_year = models.IntegerField(verbose_name="Год поступления", blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20, blank=True, null=True)
    email = models.CharField(verbose_name="e-mail", max_length=50, blank=True, null=True)
    communication_other = models.CharField(verbose_name="Другие способы коммуникации", max_length=200, blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    time_create = models.DateTimeField(verbose_name="Дата создания учетной записи", default=timezone.now)
    mentor = models.ForeignKey("mentor.Profile", related_name="students", on_delete=models.SET_NULL,
                               blank=True, null=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic if self.patronymic else ''}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        unique_together = ['name', 'surname', 'patronymic']
