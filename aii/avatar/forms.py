from django import forms
from .models import Avatar

class AvatarCustomizationForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['hair']  # add other fields as required
