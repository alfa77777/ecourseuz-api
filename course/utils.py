from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_video(video_object):
    print(video_object)
    if not video_object.path.endswith(".mp4"):
        raise ValidationError(
            _("Video format must be .mp4."),
        )


def html_message_format(courses):
    message = ""
    for course in courses:
        html = f"Course: {course.name}\n" f"Price: {course.price}\n"
        message += html

    return message
