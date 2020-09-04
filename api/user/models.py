from django.db import models


# 사용자
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    cellphone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6)
    description = models.CharField(max_length=1024, null=True)
    categories = models.CharField(max_length=1024, null=True)
    kakao_profile_img = models.CharField(max_length=1024,null=True)
    s3_profile_img = models.FileField(blank=True, null=True)
    img_flag = models.BooleanField(default=False)
    def __str__(self):
        return self.name
