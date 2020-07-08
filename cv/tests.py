from django.test import TestCase

# Create your tests here.

class CVPageTest(TestCase):
	
	def test_page_uses_cv_template(self):
		response = self.client.get("/cv/")
		self.assertTemplateUsed(response, "cv.html")
	
	def test_saves_key_skills_POST_request(self):
		response = self.client.post("/cv/", data = {"key_skill_text": "This is a new key skill."})
		self.assertIn("This is a new key skill.", response.content.decode())
		self.assertTemplateUsed(response, "cv.html")