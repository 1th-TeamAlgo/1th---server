from django.contrib import admin
from .category.models import Category
from .study.models import Study
from .user.models import User
from .study_member.models import StudyMember
from .activity_picture.models import ActivityPicture
from .schedule.models import Schedule

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Study)
admin.site.register(StudyMember)
admin.site.register(ActivityPicture)
admin.site.register(Schedule)