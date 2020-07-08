from django import forms
from .models import KeySkill

class KeySkillForm(forms.Form):
	skills_input_text = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter a new skill"}))