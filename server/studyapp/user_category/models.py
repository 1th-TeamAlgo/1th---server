from django.db import models
from ..user.models import User
from ..category.models import Category


#유저 카테고리
class UserCategory(models.Model):
    user_category_id = models.AutoField(primary_key=True)  # primary_key로 설정하면 자동생성되는 기본키 사용 안함
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


