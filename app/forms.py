from django import forms
from django.core.exceptions import ValidationError

from .models import Bypass


class BypassForm(forms.ModelForm):
    class Meta:
        model = Bypass
        fields = [
            "motiv",
            "sofer",
            "transportator",
            "cisterna",
            "tip",
            "tip_statie",
            "observatii",
        ]
        widgets = {
            "motiv": forms.Select(attrs={"class": "form-control"}),
            "sofer": forms.Select(attrs={"class": "form-control"}),
            "transportator": forms.Select(attrs={"class": "form-control"}),
            "cisterna": forms.Select(attrs={"class": "form-control"}),
            "tip": forms.Select(attrs={"class": "form-control"}),
            "tip_statie": forms.Select(attrs={"class": "form-control"}),
            "observatii": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "maxlength": 300,
                    "placeholder": "Add operational notes for this bypass case.",
                    "rows": 5,
                }
            ),
        }
        labels = {
            "motiv": "Bypass reason",
            "sofer": "Driver",
            "transportator": "Transport company",
            "cisterna": "Tanker",
            "tip": "Type",
            "tip_statie": "Station type",
            "observatii": "Notes",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["motiv"].help_text = "Select the operational reason for the bypass."
        self.fields[
            "transportator"
        ].help_text = "Pick the carrier responsible for the trip."
        self.fields[
            "observatii"
        ].help_text = "Include only the operational details needed to review the case."

    def clean(self):
        cleaned_data = super().clean()
        transportator = cleaned_data.get("transportator")
        sofer = cleaned_data.get("sofer")
        cisterna = cleaned_data.get("cisterna")

        if transportator and sofer and sofer.companie_id != transportator.id:
            raise ValidationError(
                {
                    "sofer": (
                        "The selected driver does not belong to the selected "
                        "transport company."
                    )
                }
            )

        if transportator and cisterna and cisterna.companie_id != transportator.id:
            raise ValidationError(
                {
                    "cisterna": (
                        "The selected tanker does not belong to the selected "
                        "transport company."
                    )
                }
            )

        return cleaned_data
