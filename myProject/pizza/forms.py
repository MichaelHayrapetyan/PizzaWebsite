from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['company', 'pizza_type', 'dough', 'image', 'description']
