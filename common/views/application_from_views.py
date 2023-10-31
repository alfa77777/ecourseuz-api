from django.conf import settings
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import ApplicationForm
from common.serializers.application_form import ApplicationFormSerializer
from course.models import Course
from course.utils import html_message_format


class ApplicationFormView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=ApplicationFormSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ApplicationFormSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        email = serializer.validated_data.get("email")
        category_id = serializer.validated_data.get("category")
        ApplicationForm.objects.create(name=name, email=email, category=category_id)
        courses = Course.objects.filter(categories__in=category_id.get_descendants(include_self=True))
        subject = f"Course Information CodeKaplan"
        send_mail(
            subject,
            html_message_format(courses),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        serializer.save()
        return Response({"detail": "Information about the course has been sent by email "})
