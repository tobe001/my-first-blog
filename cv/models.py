from django.db import models

# Create your models here.

class KeySkill(models.Model):
	text = models.CharField(max_length = 100, default = "")

class Education(models.Model):
	start_year = models.IntegerField(default = 0)
	end_year = models.IntegerField(default = 9999)
	institution = models.CharField(max_length = 100, default = "")
	course_title = models.CharField(max_length = 100, default = "", blank = True)
	text = models.TextField(default = "")

class Experience(models.Model):
	start_year = models.IntegerField(default = 0)
	end_year = models.IntegerField(default = 9999)
	company = models.CharField(max_length = 100, default = "")
	role = models.CharField(max_length = 100, default = "")
	text = models.TextField(default = "")

class Volunteering(models.Model):
	start_year = models.IntegerField(default = 0)
	end_year = models.IntegerField(default = 9999)
	company = models.CharField(max_length = 100, default = "")
	role = models.CharField(max_length = 100, default = "")
	text = models.TextField(default = "")

class Project(models.Model):
	text = models.TextField(default = "")

class Hobby(models.Model):
	text = models.TextField(default = "")

class Reference(models.Model):
	name = models.CharField(max_length = 100, default = "")
	relevance = models.CharField(max_length = 100, default = "")
	phone = models.CharField(max_length = 12, default = "")
	email = models.CharField(max_length = 100, default = "")

class Profile(models.Model):
	text = models.TextField(default = "")