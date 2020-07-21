from django import forms

class KeySkillForm(forms.Form):
	skills_input_text = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter a new skill"}))

class EducationForm(forms.Form):
	education_input_start_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter start year"}))
	education_input_end_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter end year"}))
	education_input_institution = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter institution name"}))
	education_input_course_title = forms.CharField(max_length = 100, required = False, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter course title"}))
	education_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter further details",
																						"rows": 4, "cols": 75}))

class ExperienceForm(forms.Form):
	experience_input_start_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter start year"}))
	experience_input_end_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter end year"}))
	experience_input_company = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter company name"}))
	experience_input_role = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter job title"}))
	experience_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter further details",
																							"rows": 4, "cols": 75}))

class VolunteeringForm(forms.Form):
	volunteering_input_start_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter start year"}))
	volunteering_input_end_year = forms.IntegerField(label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter end year"}))
	volunteering_input_company = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter company/organisation name"}))
	volunteering_input_role = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter role title"}))
	volunteering_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter further details",
																							"rows": 4, "cols": 75}))

class ProjectForm(forms.Form):
	projects_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter details of a new project or achievement",
																						"rows": 4, "cols": 75}))

class HobbyForm(forms.Form):
	hobbies_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter details of a new activity, skill or hobby",
																						"rows": 4, "cols": 75}))

class ReferenceForm(forms.Form):
	references_input_name = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter name of reference"}))
	references_input_relevance = forms.CharField(max_length = 100, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter reference's relation to you"}))
	references_input_phone = forms.CharField(max_length = 12, required = False, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter phone number"}))
	references_input_email = forms.CharField(max_length = 100, required = False, label = "", widget = forms.TextInput(attrs = {"placeholder": "Enter email address"}))

class ProfileForm(forms.Form):
	profile_input_text = forms.CharField(label = "", widget = forms.Textarea(attrs = {"placeholder": "Enter a new profile (will replace existing one)",
																						"rows": 4, "cols": 75}))