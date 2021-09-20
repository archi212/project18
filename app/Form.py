from django import forms

class ImagesForm(forms.Form):
    images=forms.ImageField()