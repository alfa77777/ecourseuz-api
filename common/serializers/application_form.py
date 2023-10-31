from rest_framework import serializers

from common.models import ApplicationForm


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = (
            "id",
            "name",
            "email",
            "category",
        )
        read_only_fields = ("id",)
