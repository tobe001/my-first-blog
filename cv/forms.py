from django import forms
from .models import KeySkill, Education

class KeySkillForm(forms.Form):
	skills_input_text = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter a new skill"}))

class EducationForm(forms.Form):
	education_input_start_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter start year"}))
	education_input_end_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter end year"}))
	education_input_institution = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter institution name"}))
	education_input_course_title = forms.CharField(max_length = 100, required = False, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter course title"}))
	education_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter further details"}))