from django.shortcuts import render, redirect
from cv.models import KeySkill
from .forms import KeySkillForm

# Create your views here.

def cv(request):
	if request.method == "POST":
		new_skill_form = KeySkillForm(request.POST)
		if new_skill_form.is_valid():
			new_skill = KeySkill()
			new_skill.text = request.POST["skills_input_text"]
			new_skill.save()
			return redirect("/cv/")
	
	skills = KeySkill.objects.all()
	skills_form = KeySkillForm()
	return render(request, "cv.html", {"skills": skills, "skills_form": skills_form})