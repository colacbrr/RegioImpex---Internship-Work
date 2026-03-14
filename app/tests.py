from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Bypass, Cisterne, MotiveBypass, Soferi, TipStatie, Tipuri, Transportatori


class BypassViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="operator",
            password="test-pass-123",
        )
        self.transportator = Transportatori.objects.create(nume="TransCo")
        self.sofer = Soferi.objects.create(nume="Driver One", companie=self.transportator)
        self.cisterna = Cisterne.objects.create(
            nr_cisterna="B-100-AAA",
            companie=self.transportator,
        )
        self.tip = Tipuri.objects.create(tip="Support")
        self.tip_statie = TipStatie.objects.create(tip_statie="Client")
        self.motiv = MotiveBypass.objects.create(motiv="Delayed loading")

    def test_bypass_requires_login(self):
        response = self.client.get(reverse("bypass"))
        self.assertEqual(response.status_code, 302)

    def test_bypass_submission_sets_logged_in_user(self):
        self.client.login(username="operator", password="test-pass-123")
        response = self.client.post(
            reverse("bypass"),
            {
                "motiv": self.motiv.pk,
                "sofer": self.sofer.pk,
                "transportator": self.transportator.pk,
                "cisterna": self.cisterna.pk,
                "tip": self.tip.pk,
                "tip_statie": self.tip_statie.pk,
                "observatii": "Created from test",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bypass.objects.count(), 1)
        self.assertEqual(Bypass.objects.first().utilizator, self.user)
