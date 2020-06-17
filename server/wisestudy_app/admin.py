from django.contrib import admin
from wisestudy_app.category.models import Category
from wisestudy_app.study.models import Study
# from wisestudy_app.category.models import User
# from wisestudy_app.category.models import StudyMember
# from wisestudy_app.category.models import ActivityPicture
# from wisestudy_app.category.models import Schedule

admin.site.register(Category)
# admin.site.register(User)
admin.site.register(Study)
# admin.site.register(StudyMember)
# admin.site.register(ActivityPicture)
# admin.site.register(Schedule)


