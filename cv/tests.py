from django.test import TestCase
from cv.models import KeySkill

# Create your tests here.

class CVPageTest(TestCase):
	
	def test_page_uses_cv_template(self):
		response = self.client.get("/cv/")
		self.assertTemplateUsed(response, "cv.html")
	
	def test_saves_key_skills_POST_request(self):
		response = self.client.post("/cv/", data = {"key_skill_text": "This is a new key skill."})
		self.assertIn("This is a new key skill.", response.content.decode())
		self.assertTemplateUsed(response, "cv.html")
	

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