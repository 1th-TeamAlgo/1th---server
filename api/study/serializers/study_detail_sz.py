from rest_framework import serializers
from ..models import Study


class StudyDetailSerializer(serializers.ModelSerializer):
    # study_members = StudyMemberSerializer(source='studymember_set', many=True, read_only=True)
    # study_activity_picture_list = ActivityPictureSerializer(source='activitypicture_set', many=True)

    class Meta:
        model = Study
        fields = ['study_id', 'category', 'title', 'limit', 'description', ]
    # class Meta:
    #     model = Study
    #     fields = ['study', 'study_members', 'study_activity_picture_list', ]

        # def get_object_with_picture(self, obj):
        #     activity_pictures = obj
        #     return self
        # def get_category_name(self, obj):
        #     return obj.category_name.name