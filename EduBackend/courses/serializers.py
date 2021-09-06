from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from . models import *



class PrerequisiteSerializer(ModelSerializer):
    class Meta:
        model = Prerequisite
        fields = '__all__'

class CourseTagsSerializer(ModelSerializer):
    class Meta:
        model = CourseTags
        fields = '__all__'
class WillLearnSerializer(ModelSerializer):
    class Meta:
        model = WillLearn
        fields = "__all__"

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class LessonSerializer(ModelSerializer):
    video = VideoSerializer(source="lesson_video", many=True, read_only=True)
    test = TestSerializer(source="lesson_test", many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    prerequisite = PrerequisiteSerializer(source="course_prerequisite", many=True, read_only=True)
    willlearn = WillLearnSerializer(source="course_willlearn", many=True, read_only=True)
    lesson = LessonSerializer(source="course_lesson", many=True, read_only=True)
    tags = CourseTagsSerializer(source="course_tags", many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
