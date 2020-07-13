from django.shortcuts import render, redirect
from cv.models import KeySkill, Education, Experience, Volunteering, Project
from .forms import KeySkillForm, EducationForm, ExperienceForm, VolunteeringForm

# Create your views here.

def cv(request):
	if request.method == "POST":
		new_skill_form = KeySkillForm(request.POST)
		new_education_form = EducationForm(request.POST)
		new_experience_form = ExperienceForm(request.POST)
		new_volunteering_form = VolunteeringForm(request.POST)
		if new_skill_form.is_valid():
			new_skill = KeySkill()
			new_skill.text = request.POST["skills_input_text"]
			new_skill.save()
			return redirect("/cv/")
		elif new_education_form.is_valid():
			new_education = Education()
			new_education.start_year = request.POST["education_input_start_year"]
			new_education.end_year = request.POST["education_input_end_year"]
			new_education.institution = request.POST["education_input_institution"]
			new_education.course_title = request.POST["education_input_course_title"]
			new_education.text = request.POST["education_input_text"]
			new_education.save()
			return redirect("/cv/")
		elif new_experience_form.is_valid():
			new_experience = Experience()
			new_experience.start_year = request.POST["experience_input_start_year"]
			new_experience.end_year = request.POST["experience_input_end_year"]
			new_experience.company = request.POST["experience_input_company"]
			new_experience.role = request.POST["experience_input_role"]
			new_experience.text = request.POST["experience_input_text"]
			new_experience.save()
			return redirect("/cv/")
		elif new_volunteering_form.is_valid():
			new_volunteering_item = Volunteering()
			new_volunteering_item.start_year = request.POST["volunteering_input_start_year"]
			new_volunteering_item.end_year = request.POST["volunteering_input_end_year"]
			new_volunteering_item.company = request.POST["volunteering_input_company"]
			new_volunteering_item.role = request.POST["volunteering_input_role"]
			new_volunteering_item.text = request.POST["volunteering_input_text"]
			new_volunteering_item.save()
			return redirect("/cv/")
		else:
			new_project = Project()
			new_project.text = request.POST["projects_input_text"]
			new_project.save()
			return redirect("/cv/")
	
	skills = KeySkill.objects.all()
	skills_form = KeySkillForm()
	education_items = Education.objects.all().order_by("-start_year")
	education_form = EducationForm()
	experience_items = Experience.objects.all().order_by("-start_year")
	experience_form = ExperienceForm()
	volunteering_items = Volunteering.objects.all().order_by("-start_year")
	volunteering_form = VolunteeringForm()
	project_items = Project.objects.all()
	return render(request, "cv.html", {"skills": skills, "skills_form": skills_form,
										"education_items": education_items, "education_form": education_form,
										"experience_items": experience_items, "experience_form": experience_form,
										"volunteering_items": volunteering_items, "volunteering_form": volunteering_form,
										"project_items": project_items})