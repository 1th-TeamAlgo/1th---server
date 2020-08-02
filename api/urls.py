from django.urls import path, include
from .category import views as category_views  # 카테고리
from .user import views as user_views  # 유저
from .study import views as study_views  # 스터디
from .study_member import views as study_member_views  # 스터디원
from .activity_picture import views as activity_picture_views  # 활동사진
from .schedule import views as schedule_views  # 일정

urlpatterns = [
    ## users ##
    path('users', user_views.UserList.as_view()),
    path('users/<int:pk>', user_views.UserDetail.as_view()),

    # categorys ##
    path('categories', category_views.CategoryList.as_view()),
    path('categories/<int:pk>', category_views.CategoryDetail.as_view()),

    # studys ##
    path('studies', study_views.StudyList.as_view()),
    path('studies/<int:pk>', study_views.StudyDetail.as_view()),

    ## study_memebers ##
    path('study_members', study_member_views.StudyMemberList.as_view()),
    path('study_members/<int:pk>', study_member_views.StudyMemeberDetail.as_view()),

    ## studys ##
    path('studies', study_views.StudyList.as_view()),
    path('studies/<int:pk>', study_views.StudyDetail.as_view()),
    path('studies/<int:pk>/members', study_views.StudyMember.as_view()),

    ## schedules ##
    path('schedules', schedule_views.ScheduleList.as_view()),
    path('schedules/<int:pk>', schedule_views.ScheduleDetail.as_view()),

    ## activity_pictures ##
    path('activity-pictures', activity_picture_views.APList.as_view()),
    path('activity-pictures/<int:pk>', activity_picture_views.APDetail.as_view()),
]
