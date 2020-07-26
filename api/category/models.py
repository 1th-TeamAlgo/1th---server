from django.db import models


# 카테고리
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  # primary_key로 설정하면 자동생성되는 기본키 사용 안함
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
