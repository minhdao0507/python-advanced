from django import forms
from .models import myProject

class proForm(forms.ModelForm):
    class Meta:
        model = myProject
        fields = ['id', 'name', 'about_pro', 'tech_used', 'source', 'status']