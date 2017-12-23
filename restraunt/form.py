from django import forms
from .models import restlist

class restcreate(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "hello":
            raise forms.ValidationError("Name Not allowed")
        return name


class restcreateclass(forms.ModelForm):
    class Meta:
        model = restlist
        fields = [
            "name",
            "location"
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "hello":
            raise forms.ValidationError("Name Not allowed")
        return name
