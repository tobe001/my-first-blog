from django.test import TestCase
from cv.models import KeySkill, Education, Experience, Volunteering, Project

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
	
	def test_saves_experience_POST_request(self):
		self.client.post("/cv/", data = {"experience_input_start_year": "2018", "experience_input_end_year": "2022", "experience_input_company": "Company", "experience_input_role": "Job Role", "experience_input_text": "Details"})
		
		self.assertEqual(Experience.objects.count(), 1)
		new_experience = Experience.objects.first()
		self.assertEqual(new_experience.start_year, 2018)
		self.assertEqual(new_experience.end_year, 2022)
		self.assertEqual(new_experience.company, "Company")
		self.assertEqual(new_experience.role, "Job Role")
		self.assertEqual(new_experience.text, "Details")
	
	def test_redirects_after_experience_POST_request(self):
		response = self.client.post("/cv/", data = {"experience_input_start_year": "2018", "experience_input_end_year": "2022", "experience_input_company": "Company", "experience_input_role": "Job Role", "experience_input_text": "Details"})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], "/cv/")
	
	def test_displays_multiple_experience_items(self):
		Experience.objects.create(start_year = 2018, end_year = 2022, company = "Company 1", role = "Job 1", text = "Details 1")
		Experience.objects.create(start_year = 2015, end_year = 2016, company = "Company 2", role = "Job 2", text = "Details 2")
		
		response = self.client.get("/cv/")
		
		self.assertIn("2018-2022: Company 1, Job 1", response.content.decode())
		self.assertIn("2015-2016: Company 2, Job 2", response.content.decode())
	
	def test_saves_volunteering_POST_request(self):
		self.client.post("/cv/", data = {"volunteering_input_start_year": "2018", "volunteering_input_end_year": "2019", "volunteering_input_company": "Company", "volunteering_input_role": "Volunteer", "volunteering_input_text": "Details"})
		
		self.assertEqual(Volunteering.objects.count(), 1)
		new_volunteering_item = Volunteering.objects.first()
		self.assertEqual(new_volunteering_item.start_year, 2018)
		self.assertEqual(new_volunteering_item.end_year, 2019)
		self.assertEqual(new_volunteering_item.company, "Company")
		self.assertEqual(new_volunteering_item.role, "Volunteer")
		self.assertEqual(new_volunteering_item.text, "Details")
	
	def test_redirects_after_volunteering_POST_request(self):
		response = self.client.post("/cv/", data = {"volunteering_input_start_year": "2018", "volunteering_input_end_year": "2019", "volunteering_input_company": "Company", "volunteering_input_role": "Volunteer", "volunteering_input_text": "Details"})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], "/cv/")
	
	def test_displays_multiple_volunteering_items(self):
		Volunteering.objects.create(start_year = 2018, end_year = 2019, company = "Company 1", role = "Volunteer 1", text = "Details 1")
		Volunteering.objects.create(start_year = 2015, end_year = 2016, company = "Company 2", role = "Volunteer 2", text = "Details 2")
		
		response = self.client.get("/cv/")
		
		self.assertIn("2018-2019: Company 1, Volunteer 1", response.content.decode())
		self.assertIn("2015-2016: Company 2, Volunteer 2", response.content.decode())
	
	def test_saves_project_POST_request(self):
		self.client.post("/cv/", data = {"projects_input_text": "Project or achievement."})
		
		self.assertEqual(Project.objects.count(), 1)
		new_project = Project.objects.first()
		self.assertEqual(new_project.text, "Project or achievement.")
	
	def test_redirects_after_project_POST_request(self):
		response = self.client.post("/cv/", data = {"projects_input_text": "Project or achievement."})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], "/cv/")
	
	def test_displays_multiple_projects(self):
		Project.objects.create(text = "Project 1")
		Project.objects.create(text = "Project 2")
		
		response = self.client.get("/cv/")
		
		self.assertIn("Project 1", response.content.decode())
		self.assertIn("Project 2", response.content.decode())
	

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