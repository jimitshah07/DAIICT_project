from django import forms

class SkillTestForm(forms.Form):
    interest = forms.CharField(label='Your Area of Interest', max_length=100)