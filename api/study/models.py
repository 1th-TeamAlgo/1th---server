from django.db import models

from ..user.models import User


# 스터디

class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    study_image = models.FileField(blank=True, null=True)
    category = models.CharField(max_length=200)
    study_members = models.ManyToManyField(User, through='StudyMember')
    study_members_count = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    limit = models.IntegerField()
    description = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
