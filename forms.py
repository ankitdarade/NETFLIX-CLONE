from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import home


class Companymaster(forms.ModelForm):
    class Meta:
        model = home
        fields = ['Firstname','Middlename','Lastname','Phone','Email','userid','Password']
