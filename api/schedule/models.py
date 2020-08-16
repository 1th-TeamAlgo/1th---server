from django.db import models
from ..study.models import Study


# 일정
class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    place = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datetime']
