from django.db import models
from ..study.models import Study
from ..user.models import User


#스터디원
class StudyMember(models.Model):
    study_member_id = models.AutoField(primary_key=True)  # primary_key로 설정하면 자동생성되는 기본키 사용 안함
    study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default= False)