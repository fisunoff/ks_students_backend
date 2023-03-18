from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=50, blank=False, null=True)
    surname = models.CharField("Фамилия", max_length=50, blank=False, null=True)
    patronymic = models.CharField("Отчество", max_length=50, blank=True, null=True)
    bio = models.TextField("Описание профиля", max_length=500, blank=True, null=True)
    birth_date = models.DateField("Дата рождения", blank=True, null=True)
    position = models.TextField("Должность", max_length=200, null=True)
    mentor = models.BooleanField("Является наставником", default=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic if self.patronymic else ''}," \
               f" {self.position if self.position else 'Должность не указана'}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        unique_together = ['name', 'surname', 'patronymic']
        ordering = ['surname', 'name', 'position']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
