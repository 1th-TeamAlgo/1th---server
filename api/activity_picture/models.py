from django.db import models

from ..study.models import Study


# 활동사진
class ActivityPicture(models.Model):
    activity_picture_id = models.AutoField(primary_key=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    activity_picture = models.FileField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.path
