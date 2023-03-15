from django.db import models
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    UNIVERSITIES = (("ChuvSU", "ЧГУ им. И.Н. Ульянова"),
                    ("politech", "Московский политех"),
                    ("other", "Прочее"))

    name = models.CharField(verbose_name="Имя", max_length=50, blank=False)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, blank=False)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    university = models.CharField(verbose_name="Место учебы", max_length=200, choices=UNIVERSITIES)
    admission_year = models.IntegerField(verbose_name="Год поступления")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=50)
    communication_other = models.CharField(verbose_name="Другие способы коммуникации", max_length=200)
    birth_date = models.DateField(verbose_name="Дата рождения")
    time_create = models.DateTimeField(verbose_name="Дата создания учетной записи", default=timezone.now)
    mentor = models.ForeignKey("mentor.Profile", related_name="students", on_delete=models.SET_NULL,
                               blank=True, null=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        unique_together = ['name', 'surname', 'patronymic']
