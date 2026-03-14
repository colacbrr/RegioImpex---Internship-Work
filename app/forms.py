from django import forms
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
