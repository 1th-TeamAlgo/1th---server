from django.db import models

from ..study.models import Study


# 활동사진
class ActivityPicture(models.Model):
    activity_picture_id = models.AutoField(primary_key=True)
    # study = models.ForeignKey(Study, related_name='activity_pictures', on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.path
