from django.test import Client, TestCase
from django.urls import reverse
from model_bakery import baker


client = Client()


class ApplicationFormViewTest(TestCase):
    def test_create_application_form(self):
        url = reverse("common:application-form")
        category = baker.make("Category")
        data = {"name": "John Doe", "email": "johndoe@example.com", "category": category.id}
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
