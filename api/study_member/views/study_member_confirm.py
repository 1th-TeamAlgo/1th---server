from django.shortcuts import get_object_or_404

from ...user.models import User
from ...study.models import Study
from ..models import StudyMember

from ..serializers.study_add_study_member_sz import StudyAddStudyMemberSerializer

from ...study.serializers.member_of_study_sz import MemberOfStudySerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.cache import cache

class StudyMemberConfirm(APIView):

    ## study 가입 신청 멤버 승인
    def post(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        str_study_id = self.str_study_id(study_id)

        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)

        self.apply_member_delete_redis(str_study_id, user_id)

        if len(StudyMember.objects.filter(study_id=study_id, user_id=user_id)) > 0:
            return Response(data=["이미 들어있다"])

        study_member_data = {
            'study': study_id,
            'user': user_id,
            'is_manager': False,
        }

        study_member_serializer = StudyAddStudyMemberSerializer(data=study_member_data)

        if study_member_serializer.is_valid():
            study_member_serializer.save()

        study_members = get_object_or_404(Study, pk=study_id)
        study_members_serializer = MemberOfStudySerializer(study_members)
        return Response(study_members_serializer.data)

    ## study 가입 신청 멤버 반려
    def delete(self, request, *args, **kwargs):
        study_id = self.kwargs['studies_id']
        str_study_id = self.str_study_id(study_id)

        user_id = request.POST.get('user_id')

        study_apply_dict = self.apply_member_delete_redis(str_study_id, user_id)

        return Response(data=study_apply_dict)

    ## 가입 승인 또는 반려 된 인원 redis에서 제거
    def apply_member_delete_redis(self, study_id, user_id):
        study_apply_dict = cache.get(study_id)

        if int(user_id) in study_apply_dict.keys():
            study_apply_dict.pop(int(user_id))
            cache.set(study_id, study_apply_dict)
            print(study_apply_dict)

        return study_apply_dict

    def str_study_id(self, study_id):
        return 'study:' + str(study_id)
