from django.contrib import admin
from studyapp.category.models import Category
from studyapp.study.models import Study
# from studyapp.category.models import User
# from studyapp.category.models import StudyMember
# from studyapp.category.models import ActivityPicture
# from studyapp.category.models import Schedule

admin.site.register(Category)
# admin.site.register(User)
admin.site.register(Study)
# admin.site.register(StudyMember)
# admin.site.register(ActivityPicture)
# admin.site.register(Schedule)


