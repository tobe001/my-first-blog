from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cv(request):
	return render(request, "cv.html", {"new_key_skill_text": request.POST.get("key_skill_text", "")})