from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class CVTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()
	
	def check_section_header(self, heading_text):
		headings = self.browser.find_elements_by_tag_name("h2")
		self.assertIn(heading_text, [heading.text for heading in headings])
	
	def check_form(self, form_id, box_ids):
		form = self.browser.find_element_by_id(form_id)
		for id in box_ids:
			box = form.find_element_by_id(id)
			self.assertIn("Enter", box.get_attribute("placeholder"))
		button = form.find_element_by_tag_name("button")
		self.assertEqual(button.text, "Save")
	
	def check_headers(self):
		self.check_section_header("Profile")
		self.check_section_header("Key Skills")
		self.check_section_header("Education")
		self.check_section_header("Work Experience")
		self.check_section_header("Voluntary Experience")
		self.check_section_header("Additional Projects and Achievements")
		self.check_section_header("Additional Activities, Skills and Hobbies")
		self.check_section_header("References")
	
	def check_forms(self):
		self.check_form("id_skills_form", ["id_skills_input_text"])
		self.check_form("id_education_form", ["id_education_input_start_year", "id_education_input_end_year", "id_education_input_institution", "id_education_input_course_title", "id_education_input_text"])
		self.check_form("id_experience_form", ["id_experience_input_start_year", "id_experience_input_end_year", "id_experience_input_company", "id_experience_input_role", "id_experience_input_text"])
		self.check_form("id_volunteering_form", ["id_volunteering_input_start_year", "id_volunteering_input_end_year", "id_volunteering_input_company", "id_volunteering_input_role", "id_volunteering_input_text"])
		self.check_form("id_projects_form", ["id_projects_input_text"])
		self.check_form("id_hobbies_form", ["id_hobbies_input_text"])
		self.check_form("id_references_form", ["id_references_input_name", "id_references_input_relevance", "id_references_input_phone", "id_references_input_email"])
	
	def check_placeholder_reference_text(self):
		references_section = self.browser.find_element_by_id("id_references")
		self.assertEqual(references_section.find_element_by_tag_name("p").text, "References available on request.")
	
	def test_fill_cv_and_retrieve(self):
		
		#User navigates to site's CV page.
		#Page title should mention the CV.
		self.browser.get("http://127.0.0.1:8000/cv")
		self.assertIn("CV", self.browser.title)
		
		#Page should include my name.
		header_text = self.browser.find_element_by_tag_name("h1").text
		self.assertIn("Thomas Beckett", header_text)
		
		#Page should contain appropriate section headers:
		#Profile
		#Key Skills
		#Education
		#Work Experience
		#Voluntary Experience
		#Additional Projects and Achievements
		#Additional Activities, Skills and Hobbies
		#References
		self.check_headers()
		
		#Page should contain input boxes for:
		#Key Skills (Text)
		#Education (Start Year, End Year, Institution, Course Title, Text)
		#Work Experience (Start Year, End Year, Company, Role, Text)
		#Voluntary Experience (Start Year, End Year, Company, Role, Text)
		#Additional Projects and Achievements (Text)
		#Additional Activities, Skills and Hobbies (Text)
		#References (Name, Relevance, Phone, Email)
		#Each form should include a "Save" button.
		self.check_forms()
		
		#In the absence of any references, the References section should read "References available on request."
		self.check_placeholder_reference_text()
		
		#User enters new Key Skill, "Programming Skills" and presses "Save" button.
		#Page should refresh and now list "Programming Skills" in the Key Skills section, along with all previous content.
		skills_form = self.browser.find_element_by_id("id_skills_form")
		skills_input_text_box = skills_form.find_element_by_id("id_skills_input_text")
		skills_input_text_box.send_keys("Programming Skills")
		skills_save_button = skills_form.find_element_by_tag_name("button")
		skills_save_button.click()
		time.sleep(1)
		
		skills_section = self.browser.find_element_by_id("id_skills")
		skill_items = skills_section.find_elements_by_tag_name("li")
		self.assertIn("Programming Skills", [skill.text for skill in skill_items])
		
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Key Skill, "Time Management" and presses "Save" button.
		#Page should refresh and now list "Time Management" in the Key Skills section, along with all previous content.
		skills_form = self.browser.find_element_by_id("id_skills_form")
		skills_input_text_box = skills_form.find_element_by_id("id_skills_input_text")
		skills_input_text_box.send_keys("Time Management")
		skills_save_button = skills_form.find_element_by_tag_name("button")
		skills_save_button.click()
		time.sleep(1)
		
		skills_section = self.browser.find_element_by_id("id_skills")
		skill_items = skills_section.find_elements_by_tag_name("li")
		self.assertIn("Time Management", [skill.text for skill in skill_items])
		self.assertIn("Programming Skills", [skill.text for skill in skill_items])
		
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Education Item (2018, 2022, University of Birmingham, MSci Mathematics and Computer Science, Description of course and results.) and presses "Save" button.
		#Page should refresh and now list "2018-2022: University of Birmingham, MSci Mathematics and Computer Science" in Education section, along with all previous content.
		#Page should also read "Description of course and results." below this.
		self.fail("Finish writing tests!")
		
		#User enters new Eductaion Item (2020, 2020, Abnormal School, (NO COURSE TITLE), Description of course and results.) and presses "Save" button.
		#Page should now refresh and list "2020: Abnormal School" in Education section, along with all previous content.
		#Page should also read "Description of course and results." below this.
		
		#Due to start year, "Abnormal School" should appear above "University of Birmingham".
		
		#User enters new Work Experience item (2015, 2016, Company 1, Intern, Description of job role.) and presses "Save" button.
		#Page should refresh and now list "2015-2016: Company 1, Intern" in Work Experience section, along with all previous content.
		#Page should also read "Description of job role." below this.
		
		#User enters new Work Experience item (2018, 2018, Company 2, Intern, Description of job role.) and presses "Save" button.
		#Page should refresh and now list "2018: Company 2, Intern" in Work Experience section, along with all previous content.
		#Page should also read "Description of job role." below this.
		
		#Due to start year, "Company 2" should appear above "Company 1".
		
		#User enters new Voluntary Experience item (2011, 2012, Company 3, Volunteer, Description of role.) and presses "Save" button.
		#Page should refresh and now list "2011-2012: Company 3, Volunteer" in Voluntary Experience section, along with all previous content.
		#Page should also read "Description of role." below this.
		
		#User enters new Voluntary Experience item (2017, 2017, Company 4, Volunteer, Description of role.) and presses "Save" button.
		#Page should refresh and now list "2017: Company 4, Volunteer" in Voluntary Experience section, along with all previous content.
		#Page should also read "Description of role." below this.
		
		#Due to start year, "Company 4" should appear above "Company 3".
		
		#User enters new Additional Projects and Achievements item, "I did a thing." and presses "Save" button.
		#Page should refresh and now list "I did a thing." in Additional Projects and Achievements section, along with all previous content.
		
		#User enters new Additional Projects and Achievements item, "I also did another thing." and presses "Save" button.
		#Page should refresh and now list "I also did another thing." in Additional Projects and Achievements section, along with all previous content.
		
		#User enters new Additional Activites, Skills and Hobbies item, "I can do stuff." and presses "Save" button.
		#Page should refresh and now list "I can do stuff." in Additional Activites, Skills and Hobbies section, along with all previous content.
		
		#User enters new Additional Activities, Skills and Hobbies item, "I can also do things." and presses "Save" button.
		#Page should refresh and now list "I can also do things." in Additional Activities, Skills and Hobbies section, along with all previous content.
		
		#User enters new References item (Person 1, Academic Tutor, 00000 000000, person@email,com) and presses "Save" button.
		#Page should refresh and now list "Person 1, Academic Tutor. Phone: 00000 000000, Email: person@email.com" in References section,
		#along with all previous content except for "References are available on request.", which should no longer be displayed.
		
		#User enters new References item (Person 2, Work Experience Supervisor, (NO PHONE), (NO EMAIL)) and presses "Save" button.
		#Page should refresh and now list "Person 2, Work Experience Supervisor." in References section, along with all previous content.
		
		#User navigates to CV page again.
		#All previous content should still be there.
		
		#User exits browser, concluding test.
	

if __name__ == "__main__":
	unittest.main(warnings = "ignore")