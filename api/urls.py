from django.urls import path
from .signup import views as signup_vies
from .accounts import views as kakao_account

from .user.views.user_list import UserList
from .user.views.user_image_upload import UserImageUpload
from .user.views.user_schedule_list import UserScheduleList

from .study.views.study_list import StudyList
from .study.views.study_detail import StudyDetail
from .study.views.study_schedule import StudySchedule
from .study.views.study_schedule_detail import StudyScheduleDetail
from .study.views.study_member_list import Study_StudyMember
from .study.views.study_member_detail import Study_StudyMemberDetail

from .study_member.views.study_member_apply import StudyMemberApply
from .study_member.views.study_member_confirm import StudyMemberConfirm

from .study.views.study_activity_picture import StudyActivity_pictures
from .study.views.study_activity_picture_detail import StudyActivityPicturesDetail
app_name = 'accounts'

urlpatterns = [
    ## 안드에 jwt 없으면 회원 가입으로 넘어온다고 했음 ##
    ## 회원가입 api ##
    path('oauth/token', kakao_account.KakaoAccount.as_view(), name='kakao_account'),
    path('signup', signup_vies.UserSignUp.as_view()),

    ## users ##
    path('users', UserList.as_view()),
    path('users/image', UserImageUpload.as_view()),
    path('users/schedules', UserScheduleList.as_view()),

    ## studys ##
    path('studies', StudyList.as_view()),
    path('studies/<int:studies_id>', StudyDetail.as_view()),
    path('studies/<int:studies_id>/schedules', StudySchedule.as_view()),
    path('studies/<int:studies_id>/schedules/<int:schedules_id>', StudyScheduleDetail.as_view()),
    path('studies/<int:studies_id>/members', Study_StudyMember.as_view()),
    path('studies/<int:studies_id>/members/<int:study_members_id>', Study_StudyMemberDetail.as_view()),
    path('studies/<int:studies_id>/members/apply', StudyMemberApply.as_view()),
    path('studies/<int:studies_id>/members/comfirm', StudyMemberConfirm.as_view()),
    path('studies/<int:studies_id>/pictures', StudyActivity_pictures.as_view()),
    path('studies/<int:studies_id>/pictures/<int:activity_pictures_id>',StudyActivityPicturesDetail.as_view()),

]
