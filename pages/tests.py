from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app.models import (
    Bypass,
    Cisterne,
    MotiveBypass,
    Soferi,
    TipStatie,
    Tipuri,
    Transportatori,
)


class DashboardViewTests(TestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_renders_for_authenticated_user(self):
        get_user_model().objects.create_user(
            username="dashboard-user",
            password="test-pass-123",
        )
        self.client.login(username="dashboard-user", password="test-pass-123")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_includes_recent_entries(self):
        user = get_user_model().objects.create_user(
            username="metrics-user",
            password="test-pass-123",
        )
        transportator = Transportatori.objects.create(nume="DashTrans")
        sofer = Soferi.objects.create(
            nume="Dash Driver",
            companie=transportator,
        )
        cisterna = Cisterne.objects.create(
            nr_cisterna="B-200-BBB",
            companie=transportator,
        )
        tip = Tipuri.objects.create(tip="Urgent")
        tip_statie = TipStatie.objects.create(tip_statie="Depot")
        motiv = MotiveBypass.objects.create(motiv="Maintenance")
        Bypass.objects.create(
            motiv=motiv,
            sofer=sofer,
            transportator=transportator,
            cisterna=cisterna,
            tip=tip,
            tip_statie=tip_statie,
            utilizator=user,
            observatii="Recent dashboard entry",
        )

        self.client.login(username="metrics-user", password="test-pass-123")
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Recent dashboard entry")
