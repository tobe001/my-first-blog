from django.test import TestCase
from cv.models import KeySkill

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