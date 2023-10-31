from rest_framework import serializers

from category.serializers import CategorySerializer
from course.models import Course, CourseContent, CourseSection, Review
from users.models import User


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "slug", "image", "name", "desc", "level", "price")


class CourseSerializerForLog(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = ("title", "description", "video", "source", "is_public", "time")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context["request"]
        if instance.video:
            data["video"] = request.build_absolute_uri(instance.video.url)
        return data


class CourseSectionSerializer(serializers.ModelSerializer):
    contents = CourseContentSerializer(many=True)

    class Meta:
        model = CourseSection
        fields = ("title", "time", "contents")


class CourseAuthorSerializer(serializers.ModelSerializer):
    """
    Faqat course author emas, User malumotlarini olish uchun ham ishlatiladi.
    """

    class Meta:
        model = User
        fields = ("id", "full_name", "profile_picture", "job")
        extra_kwargs = {"job": {"read_only": True}}


class CourseDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    categories = CategorySerializer(many=True)
    author = CourseAuthorSerializer()

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "slug",
            "author",
            "image",
            "video",
            "desc",
            "price",
            "discount",
            "level",
            "categories",
            "rates",
        )


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("rate", "comment", "created_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = CourseAuthorSerializer(instance.user).data
        return data


class CourseContentUploadSerializer(serializers.ModelSerializer):
    video = serializers.FileField(required=True)
    section_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CourseContent
        fields = ['title', 'description', 'video', 'is_public', 'section_id', 'position']

    def create(self, validated_data):
        section_id = validated_data.pop('section_id')
        section = CourseSection.objects.get(pk=section_id)
        validated_data['section'] = section
        return super().create(validated_data)


class ImportFileSerializer(serializers.Serializer):
    file = serializers.FileField()
