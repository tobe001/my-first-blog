from django.db import models

# Create your models here.

class KeySkill(models.Model):
	text = models.CharField(max_length = 100, default = "")