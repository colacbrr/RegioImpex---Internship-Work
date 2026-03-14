from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse


class UserViewsTests(TestCase):
    def setUp(self):
        self.password = "test-pass-123"
        self.admin_group = Group.objects.create(name="Administratori")
        self.admin_user = get_user_model().objects.create_user(
            username="adminuser",
            password=self.password,
            is_staff=True,
        )
        self.admin_user.groups.add(self.admin_group)

    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_admin_can_create_operator(self):
        self.client.login(username="adminuser", password=self.password)
        response = self.client.post(
            reverse("add_user"),
            {
                "username": "newoperator",
                "email": "newoperator@example.com",
                "phone_number": "123456789",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            get_user_model().objects.filter(username="newoperator").exists()
        )

    def test_non_admin_cannot_access_user_list(self):
        operator = get_user_model().objects.create_user(
            username="operator-user",
            password=self.password,
        )
        self.client.login(username=operator.username, password=self.password)
        response = self.client.get(reverse("user_list"))

        self.assertEqual(response.status_code, 302)

    def test_admin_can_search_user_list(self):
        get_user_model().objects.create_user(
            username="filtered-user",
            email="filtered@example.com",
            password=self.password,
        )
        self.client.login(username="adminuser", password=self.password)
        response = self.client.get(reverse("user_list"), {"q": "filtered"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "filtered-user")
