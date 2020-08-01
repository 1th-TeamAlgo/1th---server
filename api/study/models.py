from django.db import models
from ..category.models import Category
from ..user.models import User


# 스터디

class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name='study', on_delete=models.CASCADE)
    study_members = models.ManyToManyField(User, through='StudyMember')
    title = models.CharField(max_length=50)
    limit = models.IntegerField()
    description = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
