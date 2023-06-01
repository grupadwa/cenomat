from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from register.homepage_view import homepage
from register.about_us_view import about


class MainPageViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page_view(self):
        request = self.factory.get(reverse("homepage"))
        response = homepage(request)

    def test_about(self):
        request = self.factory.get(reverse("about"))
        response = about(request)

    def test_features_view(self):
        response = self.client.get(reverse("features"))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)