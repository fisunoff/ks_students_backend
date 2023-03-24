from django.db import models
from django.utils import timezone

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField("Название тега", max_length=200)
    time_create = models.DateTimeField("Дата создания", default=timezone.now)

    def __str__(self):
        return self.tag_name

    def get_count(self):
        return self.interactions_by_tag.count()

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        unique_together = ['tag_name', ]
        ordering = ['tag_name', ]
