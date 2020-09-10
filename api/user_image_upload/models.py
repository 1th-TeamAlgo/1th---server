from django.db import models


# 사용자
class TestImage(models.Model):
    s3_profile_img = models.FileField(blank=True, null=True)
