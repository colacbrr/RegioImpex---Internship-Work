from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class DashboardViewTests(TestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_renders_for_authenticated_user(self):
        user = get_user_model().objects.create_user(
            username="dashboard-user",
            password="test-pass-123",
        )
        self.client.login(username="dashboard-user", password="test-pass-123")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
