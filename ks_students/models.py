from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="Имя", max_length=50, blank=False)
    surname = models.CharField(verbose_name="Фамилия", max_length=50, blank=False)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    university = models.CharField(verbose_name="Место учебы", max_length=200)
    admission_year = models.IntegerField(verbose_name="Год поступления")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=50)
    communication_other = models.CharField(verbose_name="Другие способы коммуникации", max_length=200)
    birth_date = models.DateField(verbose_name="Дата рождения")
    time_create = models.DateTimeField(verbose_name="Дата создания учетной записи", default=timezone.now)
    mentor = models.ForeignKey("Profile", verbose_name="Наставник", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=50, blank=False, null=True)
    surname = models.CharField("Фамилия", max_length=50, blank=False, null=True)
    patronymic = models.CharField("Отчество", max_length=50, blank=True, null=True)
    bio = models.TextField("Описание профиля", max_length=500, blank=True, null=True)
    birth_date = models.DateField("Дата рождения", blank=True, null=True)
    position = models.TextField("Должность", max_length=200, null=True)
    mentor = models.BooleanField("Является наставником", default=False)

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Interaction(models.Model):
    interaction_name = models.TextField("Название")
    type = models.ForeignKey("InteractionType", verbose_name="Тип взаимодействия", on_delete=models.SET_NULL, null=True)
    mentor = models.ForeignKey("Profile", verbose_name="Наставник", on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey("Student", verbose_name="Студент", on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField("Дата создания", default=timezone.now)
    time_edit = models.DateTimeField("Дата последнего изменения", default=timezone.now)
    start_date = models.DateField("Дата начала", blank=True, null=True)
    end_date = models.DateField("Дата окончания", blank=True, null=True)
    status = models.ForeignKey("Status", verbose_name="Статус", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.interaction_name

    class Meta:
        verbose_name = "Взаимодействие"
        verbose_name_plural = "Взаимодействия"


class InteractionType(models.Model):
    type_name = models.TextField("Название типа взаимодействия")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Тип взаимодействия"
        verbose_name_plural = "Типы взаимодействия"


class Status(models.Model):
    status_name = models.TextField("Название статуса")

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
