from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "category",
            "location",
            "date",
            "image",
            "status",
        ]

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }