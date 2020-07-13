from django.contrib import admin
from .models import KeySkill, Education, Experience, Volunteering

# Register your models here.

admin.site.register(KeySkill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Volunteering)