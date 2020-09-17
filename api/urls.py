from django.urls import path, include
from .user import views as user_views  # 유저
from .study import views as study_views  # 스터디
from .schedule import views as schedule_views  # 일정

from api.accounts import views as accounts_views  # 카카오로그인
from .accounts import views as kakao_account
from .signup import views as signup_vies
from .user_image_upload import views as UserImage
from .study_member import views as study_member

app_name = 'accounts'

urlpatterns = [
    ## 안드에 jwt 없으면 회원 가입으로 넘어온다고 했음 ##
    ## 회원가입 api ##
    path('signup', signup_vies.UserSignUp.as_view()),

    ## users ##
    path('users', user_views.UserList.as_view()),
    ## profile 이미지 변경할때 사용하는 api
    path('users/image', UserImage.UserImage.as_view()),
    path('users/schedules', user_views.UserScheduleList.as_view()),
    # path('users/<int:pk>', user_views.UserDetail.as_view()),

    # categorys(deprecate) ##
    # path('categories', category_views.CategoryList.as_view()),
    # path('categories/<int:pk>', category_views.CategoryDetail.as_view()),

    # studys ##
    # path('studies', study_views.StudyList.as_view()),
    # path('studies/<int:pk>', study_views.StudyDetail.as_view()),

    ## study_memebers(deprecate) ##
    # path('study_members', study_member_views.StudyMemberList.as_view()),
    # path('study_members/<int:pk>', study_member_views.StudyMemeberDetail.as_view()),

    ## studys ##
    path('studies', study_views.StudyList.as_view()),
    # path('studies/<int:pk>', study_views.StudyDetail.as_view()),
    # path('studies/<int:pk>/members', study_views.StudyMember.as_view()),
    # path('studies/<int:pk>/activity-pictures', study_views.Activity_pictures.as_view()),
    path('studies/<int:studies_id>', study_views.StudyDetail.as_view()),
    # path('studies/<int:studies_id>/members', study_views.StudyMember.as_view()),
    path('studies/<int:studies_id>/schedules', study_views.StudySchedule.as_view()),
    path('studies/<int:studies_id>/schedules/<int:schedules_id>', study_views.StudyScheduleDetail.as_view()),
    path('studies/<int:studies_id>/pictures', study_views.StudyActivity_pictures.as_view()),
    path('studies/<int:studies_id>/pictures/<int:activity_pictures_id>',
         study_views.StudyActivity_picturesDetail.as_view()),
    path('studies/<int:studies_id>/members', study_views.Study_StudyMember.as_view()),
    path('studies/<int:studies_id>/members/<int:study_members_id>', study_views.Study_StudyMemberDetail.as_view()),

    ##스터디 가입 신청
    path('studies/<int:studies_id>/members/apply', study_member.StudyMemberJoin.as_view()),

    ## 스터디 가입 승인 (post), 스터디 가입 반려 (delete)
    path('studies/<int:studies_id>/members/comfirm', study_member.StudyMemberConfirm.as_view()),
    ## schedules ##
    # path('schedules', schedule_views.ScheduleList.as_view()),
    # path('schedules/<int:pk>', schedule_views.ScheduleDetail.as_view()),

    ## activity_pictures(Update 필요) ##
    # path('activity-pictures', activity_picture_views.APList.as_view()),
    # path('activity-pictures/<int:pk>', activity_picture_views.APDetail.as_view()),

    # 카카오 로그인
    path('oauth/token', kakao_account.KakaoAccount.as_view(), name='kakao_account'),
]
