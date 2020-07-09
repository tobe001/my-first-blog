from django.test import TestCase
from cv.models import KeySkill, Education

# Create your tests here.

class CVPageTest(TestCase):
	
	def test_page_uses_cv_template(self):
		response = self.client.get("/cv/")
		self.assertTemplateUsed(response, "cv.html")
	
	def test_saves_key_skills_POST_request(self):
		self.client.post("/cv/", data = {"skills_input_text": "This is a new key skill."})
		
		self.assertEqual(KeySkill.objects.count(), 1)
		new_key_skill = KeySkill.objects.first()
		self.assertEqual(new_key_skill.text, "This is a new key skill.")
	
	def test_redirects_after_key_skills_POST_request(self):
		response = self.client.post("/cv/", data = {"skills_input_text": "This is a new key skill."})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], "/cv/")
	
	def test_dont_save_blank_key_skills(self):
		self.client.get("/cv/")
		self.assertEqual(KeySkill.objects.count(), 0)
	
	def test_displays_multiple_key_skills(self):
		KeySkill.objects.create(text = "Skill 1")
		KeySkill.objects.create(text = "Skill 2")
		
		response = self.client.get("/cv/")
		
		self.assertIn("Skill 1", response.content.decode())
		self.assertIn("Skill 2", response.content.decode())
	
	def test_saves_education_POST_request(self):
		self.client.post("/cv/", data = {"education_input_start_year": "2018", "education_input_end_year": "2022", "education_input_institution": "Institution", "education_input_course_title": "Course", "education_input_text": "Details"})
		
		self.assertEqual(Education.objects.count(), 1)
		new_education = Education.objects.first()
		self.assertEqual(new_education.start_year, 2018)
		self.assertEqual(new_education.end_year, 2022)
		self.assertEqual(new_education.institution, "Institution")
		self.assertEqual(new_education.course_title, "Course")
		self.assertEqual(new_education.text, "Details")
	
	def test_redirects_after_education_POST_request(self):
		response = self.client.post("/cv/", data = {"education_input_start_year": "2018", "education_input_end_year": "2022", "education_input_institution": "Institution", "education_input_course_title": "Course", "education_input_text": "Details"})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], "/cv/")
	
	def test_displays_multiple_education_items(self):
		Education.objects.create(start_year = 2018, end_year = 2022, institution = "Institution 1", course_title = "Course 1", text = "Details 1")
		Education.objects.create(start_year = 2011, end_year = 2016, institution = "Institution 2", course_title = "Course 2", text = "Details 2")
		
		response = self.client.get("/cv/")
		
		self.assertIn("2018-2022: Institution 1, Course 1", response.content.decode())
		self.assertIn("2011-2016: Institution 2, Course 2", response.content.decode())
	

class ModelsTest(TestCase):
	
	def test_save_and_retrieve_key_skills(self):
		skill1 = KeySkill()
		skill1.text = "The first skill"
		skill1.save()
		
		skill2 = KeySkill()
		skill2.text = "The second skill"
		skill2.save()
		
		saved_skills = KeySkill.objects.all()
		self.assertEqual(saved_skills.count(), 2)
		
		saved_skill1 = saved_skills[0]
		saved_skill2 = saved_skills[1]
		self.assertEqual(saved_skill1.text, "The first skill")
		self.assertEqual(saved_skill2.text, "The second skill")