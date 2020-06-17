from django.db import models
from ..study.models import Study


#일정
class Schedule(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
    datetime = models.DateField()
    place = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title



