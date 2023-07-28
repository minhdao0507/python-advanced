from django import forms

class AddUser(forms.Form):
    name = forms.CharField(label='Name',max_length=50)
    age = forms.IntegerField(label='Age')
    address = forms.CharField(label='Address')
    mobile_number = forms.CharField(label='Mobile number',max_length=10)