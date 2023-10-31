import pytest
from django.test import TestCase
from django.urls import reverse


@pytest.mark.django_db
class CourseListViewTest(TestCase):
    url = reverse("course-api")
    course_data = {
        "name": "Python",
        "slug": "test_slug",
        "desc": "test_desc",
        "price": 2000,
        "discount": 0,
        "level": "Jun",
        "author": "John Doe",
        "categories": "IT",
    }

    def test_list_course(self):
        self.response = self.client.post(self.url, self.course_data)
