from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from category.models import Category
from common.models import BaseModel
from users.models import User

from .utils import validate_video


class Course(BaseModel):
    class CourseLevels(models.TextChoices):
        BEGINNER = "beginner", _("Beginner")
        INTERMEDIATE = "intermediate", _("Intermediate")
        ADVANCED = "advanced", _("Advanced")

    name = models.CharField(_("Name"), max_length=250)
    slug = models.SlugField(unique=True)
    desc = RichTextUploadingField(
        _("Description"),
    )
    price = models.PositiveIntegerField(_("Price"))
    discount = models.PositiveIntegerField()
    level = models.CharField(max_length=32, choices=CourseLevels.choices, default=CourseLevels.BEGINNER)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_authored")
    categories = models.ManyToManyField(Category, related_name="courses")
    image = models.ImageField(upload_to="course_picture/", blank=True, null=True)
    video = models.FileField(upload_to="course_video/", blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def rates(self):
        review_count = self.reviews.count()
        rates = {
            "1": self.reviews.filter(rate=1).count(),
            "2": self.reviews.filter(rate=2).count(),
            "3": self.reviews.filter(rate=3).count(),
            "4": self.reviews.filter(rate=4).count(),
            "5": self.reviews.filter(rate=5).count(),
        }

        for rate, count in rates.items():
            rates[rate] = round((count / review_count) * 100 if review_count > 0 else 0, 1)
        rates["total_rates"] = review_count
        rates["average"] = round(self.reviews.aggregate(models.Sum("rate")).get("rate__sum") / review_count, 1)
        return rates


class CourseContent(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to="course_content/", validators=[validate_video], null=True, blank=True)
    source = models.URLField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    time = models.PositiveIntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="contents")
    section = models.ForeignKey("CourseSection", on_delete=models.CASCADE, related_name="contents", null=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title

    @property
    def get_video_url(self):  # noqa
        return self.video.path


class Rate(models.Choices):
    CHOICE_ONE = 1
    CHOICE_TWO = 2
    CHOICE_THREE = 3
    CHOICE_FOUR = 4
    CHOICE_FIVE = 5


class CourseApply(BaseModel):
    class ApplyStatus(models.Choices):
        UNPAID = _("Unpaid")
        PAID = _("Paid")

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="applies")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="applies")
    status = models.CharField(max_length=20, choices=ApplyStatus.choices, default=ApplyStatus.UNPAID)

    def __str__(self):
        return str(self.user)

    class Meta:
        unique_together = ["user", "course"]


class Review(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reviews")
    rate = models.IntegerField(choices=Rate.choices)
    comment = models.CharField(max_length=400)

    def __str__(self):
        return str(self.user.first_name)

    @property
    def reviews_rate(self):
        return


class CourseProgress(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="course_progress")
    course_content = models.ForeignKey("course.CourseContent", on_delete=models.CASCADE, related_name="progress")
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ["user", "course_content"]


class CourseSection(models.Model):
    title = models.CharField(max_length=126)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    @property
    def time(self):
        return self.contents.aggregate(models.Sum("time")).get("time__sum")
