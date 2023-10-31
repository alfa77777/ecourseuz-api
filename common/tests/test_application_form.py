import pytest
from django.urls import reverse
from model_bakery import baker

from common.models import Blog


@pytest.mark.django_db
class TestApplicationFormView:
    def test_create_application_form1(self, client):
        category = baker.make("Category")
        url = reverse("common:application-form")
        data = {"name": "John Doe", "email": "johndoe@example.com", "category": category.id}

        response = client.post(url, data=data)
        assert response.status_code == 200


class TestBlogView:
    @pytest.mark.django_db
    def test_blog_list(self, client, new_blog):
        url = reverse("common:blog-list")

        response = client.get(url)

        assert response.status_code == 200
        assert len(response.data["results"]) == Blog.objects.count()
        assert response.data["results"][0]["title"] == new_blog.title
