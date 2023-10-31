import cv2
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from pytube import YouTube

from common.models import Log
from course.models import Course, CourseContent
from course.serializers import CourseSerializerForLog


@receiver(pre_delete, sender=Course)
def save_course_data_to_log(sender, instance, **kwargs):  # noqa
    content_type = ContentType.objects.get_for_model(Course)
    old_data = CourseSerializerForLog(instance).data
    Log.objects.create(content_type=content_type, object_id=instance.id, action=Log.Actions.DELETE, data=old_data)


@receiver(post_save, sender=CourseContent)
def save_course_content_video_time(sender, instance, **kwargs):  # noqa
    if instance.video:
        video = cv2.VideoCapture(instance.video.path)
        frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = video.get(cv2.CAP_PROP_FPS)
        if not (frames == 0 or fps == 0):
            CourseContent.objects.filter(pk=instance.pk).update(time=round(frames / fps))
    elif instance.source:
        CourseContent.objects.filter(pk=instance.pk).update(time=YouTube(instance.source).length)
