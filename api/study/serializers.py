from rest_framework import serializers
from .models import Study
from ..activity_picture.models import ActivityPicture
from ..activity_picture.serializers import ActivityPictureSerializer
from ..study_member.serializers import StudyMemberSerializer
from ..schedule.serializers import ScheduleSerializer


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'description', ]


# class ActivityPictureStudySerializer(serializers.ModelSerializer):
#     activity_picture_id = ActivityPictureSerializer(source='activity_picture.activity_picture_id')
#     path = ActivityPictureSerializer(source='activity_picture.path')
#
#     class Meta:
#         model = Study
#         fields = ['activity_picture_id', 'path']


class StudyDetailSerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True, read_only=True)
    study_activity_picture_list = ActivityPictureSerializer(source='activitypicture_set', many=True)
    # activity_picture_list = Activity_pictureOfStudySerializer(source='activitypicture_set', many=True, read_only=True)

    # category_name = serializers.ReadOnlyField(source='category.name')
    # activity_pictures = ActivityPictureSerializer(many=True, read_only=True)

    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'description', 'study_members', 'study_activity_picture_list', ]
        # fields = ['study_id', 'category', 'title', 'limit', 'description', 'study_members', ]

        # def get_object_with_picture(self, obj):
        #     activity_pictures = obj
        #     return self
        # def get_category_name(self, obj):
        #     return obj.category_name.name


class Activity_pictureOfStudySerializer(serializers.ModelSerializer):
    study_activity_picture = ActivityPictureSerializer(source='activitypicture_set', many=True)

    class Meta:
        model = Study
        fields = ['study_activity_picture', ]


class MemberOfStudySerializer(serializers.ModelSerializer):
    study_members = StudyMemberSerializer(source='studymember_set', many=True)

    class Meta:
        model = Study
        fields = ['study_members', ]


class ScheduleOfStudySerializer(serializers.ModelSerializer):
    study_schedule = ScheduleSerializer(source='schedule_set', many=True)

    class Meta:
        model = Study
        fields = ['study_schedule', ]
