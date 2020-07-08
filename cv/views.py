from django.shortcuts import render, redirect
from cv.models import KeySkill

# Create your views here.

def cv(request):
	if request.method == "POST":
		KeySkill.objects.create(text = request.POST["key_skill_text"])
		return redirect("/cv/")
	
	skills = KeySkill.objects.all()
	return render(request, "cv.html", {"skills": skills})