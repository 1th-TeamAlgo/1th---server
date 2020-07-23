from django.db import models

#카테고리
class Category(models.Model):
    category_id = models.AutoField(primary_key=True) # primary_key로 설정하면 자동생성되는 기본키 사용 안함
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
#
# #사용자
# class User(models.Model):
#     #user_id = models.IntegerField(primary_key=True, default= 1)
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)
#     birthday = models.DateField()
#     cellphone = models.CharField(max_length=20)
#     gender = models.CharField(max_length=1)
#
#     def __str__(self):
#         return self.name
#
#
# #스터디원
# class StudyMember(models.Model):
#     #study_member_id = models.IntegerField(primary_key=True)
#     study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
#     users_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_manager = models.BooleanField()
#
#
# #활동사진
# class ActivityPicture(models.Model):
#     #activity_picture_id = models.IntegerField(primary_key=True)
#     study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
#     path = models.CharField(max_length=200)
#     create_at = models.DateTimeField(auto_now_add =True)
#     update_at = models.DateTimeField(auto_now = True)
#
# #일정
# class Schedule(models.Model):
#     #schedule_id = models.IntegerField(primary_key=True)
#     study_id = models.ForeignKey(Study, on_delete=models.CASCADE)
#     datetime = models.DateField()
#     place = models.CharField(max_length=20)
#     address = models.CharField(max_length=200)
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.title
