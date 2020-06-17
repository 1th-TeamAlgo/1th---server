from django.urls import path, include
from wisestudy_app.category import views as category_views #카테고리
from wisestudy_app.user import views as user_views #유저
from wisestudy_app.user_category import views as user_category_views #유저 카테고리
from wisestudy_app.study import views as study_views #스터디
from wisestudy_app.study_member import views as study_member_views #스터디원
from wisestudy_app.activity_picture import views as activity_picture_views #활동사진
from wisestudy_app.schedule import views as schedule_views #일정

#카테고리
category_patterns = [
    path('', category_views.getAllOrCreateCategory),
    path('/<int:id>', category_views.getCategory)
]

#유저
user_patterns = [
    path('', user_views.getAllOrCreateUser),
    path('/<int:id>', user_views.getUser)
]

#유저 카테고리
user_category_patterns = [
    path('', user_category_views.getAllOrCreateUserCategory),
    path('/<int:id>', user_category_views.getUserCategory)
]

#스터디
study_patterns = [
    path('', study_views.getAllOrCreateStudy),
    path('/<int:id>', study_views.getStudy)
]

#스터디원
study_member_patterns = [
    path('', study_member_views.getAllOrCreateStudyMember),
    path('/<int:id>', study_member_views.getStudyMember)


]

#활동사진
activity_picture_patterns = [
    path('', activity_picture_views.getAllOrCreateActivityPicture),
    path('/<int:id>', activity_picture_views.getActivityPicture)
]

#일정
schedule_patterns = [
    path('', schedule_views.getAllOrCreateSchedule),
    path('/<int:id>', schedule_views.getSchedule)
]


urlpatterns = [
    path('/category', include(category_patterns)),
    path('/user', include(user_patterns)),
    path('/user_category', include(user_category_patterns)),
    path('/study', include(study_patterns)),
    path('/study_member', include(study_member_patterns)),
    path('/activity_picture', include(activity_picture_patterns)),
    path('/schedule', include(schedule_patterns)),
]


