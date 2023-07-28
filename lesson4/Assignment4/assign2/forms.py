from django.forms import ModelForm
from .models import Animal

class AnimalForm(ModelForm):
    class META:
        model = Animal
        fields = ['name', 'age', 'color']