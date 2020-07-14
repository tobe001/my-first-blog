from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CVTest(LiveServerTestCase):
	
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
	
	def check_for_key_skills(self, skills):
		skills_section = self.browser.find_element_by_id("id_skills")
		skill_items = skills_section.find_elements_by_tag_name("li")
		for skill in skills:
			self.assertIn(skill, [item.text for item in skill_items])
	
	def check_for_education_items_in_order(self, items):
		education_section = self.browser.find_element_by_id("id_education")
		for i in range(len(items)):
			education_item = education_section.find_element_by_id("id_education_" + str(i+1))
			education_header = education_item.find_element_by_tag_name("h3").text
			self.assertEqual(education_header, items[i]["header"])
			education_text = education_item.find_element_by_tag_name("p").text
			self.assertEqual(education_text, items[i]["text"])
	
	def check_for_experience_items_in_order(self, items):
		experience_section = self.browser.find_element_by_id("id_experience")
		for i in range(len(items)):
			experience_item = experience_section.find_element_by_id("id_experience_" + str(i+1))
			experience_header = experience_item.find_element_by_tag_name("h3").text
			self.assertEqual(experience_header, items[i]["header"])
			experience_text = experience_item.find_element_by_tag_name("p").text
			self.assertEqual(experience_text, items[i]["text"])
	
	def check_for_volunteering_items_in_order(self, items):
		volunteering_section = self.browser.find_element_by_id("id_volunteering")
		for i in range(len(items)):
			volunteering_item = volunteering_section.find_element_by_id("id_volunteering_" + str(i+1))
			volunteering_header = volunteering_item.find_element_by_tag_name("h3").text
			self.assertEqual(volunteering_header, items[i]["header"])
			volunteering_text = volunteering_item.find_element_by_tag_name("p").text
			self.assertEqual(volunteering_text, items[i]["text"])
	
	def check_for_projects(self, projects):
		projects_section = self.browser.find_element_by_id("id_projects")
		project_items = projects_section.find_elements_by_tag_name("li")
		for project in projects:
			self.assertIn(project, [item.text for item in project_items])
		
	def check_for_hobbies(self, hobbies):
		hobbies_section = self.browser.find_element_by_id("id_hobbies")
		hobby_items = hobbies_section.find_elements_by_tag_name("li")
		for hobby in hobbies:
			self.assertIn(hobby, [item.text for item in hobby_items])
	
	def test_fill_cv_and_retrieve(self):
		
		#User navigates to site's CV page.
		#Page title should mention the CV.
		self.browser.get(self.live_server_url + "/cv/")
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
		
		self.check_for_key_skills(["Programming Skills"])
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
		
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Education Item (2018, 2022, University of Birmingham, MSci Mathematics and Computer Science, Description of course and results.) and presses "Save" button.
		#Page should refresh and now list "2018-2022: University of Birmingham, MSci Mathematics and Computer Science" in Education section, along with all previous content.
		#Page should also read "Description of course and results." below this.
		education_form = self.browser.find_element_by_id("id_education_form")
		education_input_start_year_box = education_form.find_element_by_id("id_education_input_start_year")
		education_input_start_year_box.send_keys("2018")
		education_input_end_year_box = education_form.find_element_by_id("id_education_input_end_year")
		education_input_end_year_box.send_keys("2022")
		education_input_institution_box = education_form.find_element_by_id("id_education_input_institution")
		education_input_institution_box.send_keys("University of Birmingham")
		education_input_course_box = education_form.find_element_by_id("id_education_input_course_title")
		education_input_course_box.send_keys("MSci Mathematics and Computer Science")
		education_input_text_box = education_form.find_element_by_id("id_education_input_text")
		education_input_text_box.send_keys("Description of course and results.")
		education_save_button = education_form.find_element_by_tag_name("button")
		education_save_button.click()
		time.sleep(1)
		
		education_item_1 = {"header": "2018-2022: University of Birmingham, MSci Mathematics and Computer Science", "text": "Description of course and results."}
		self.check_for_education_items_in_order([education_item_1])
		
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Eductaion Item (2020, 2020, Abnormal School, (NO COURSE TITLE), Description of course and results.) and presses "Save" button.
		#Page should now refresh and list "2020: Abnormal School" in Education section, along with all previous content.
		#Page should also read "Description of course and results." below this.
		education_form = self.browser.find_element_by_id("id_education_form")
		education_input_start_year_box = education_form.find_element_by_id("id_education_input_start_year")
		education_input_start_year_box.send_keys("2020")
		education_input_end_year_box = education_form.find_element_by_id("id_education_input_end_year")
		education_input_end_year_box.send_keys("2020")
		education_input_institution_box = education_form.find_element_by_id("id_education_input_institution")
		education_input_institution_box.send_keys("Abnormal School")
		education_input_text_box = education_form.find_element_by_id("id_education_input_text")
		education_input_text_box.send_keys("Description of course and results.")
		education_save_button = education_form.find_element_by_tag_name("button")
		education_save_button.click()
		time.sleep(1)
		
		education_item_2 = {"header": "2020: Abnormal School", "text": "Description of course and results."}
		#Due to start year, "Abnormal School" should appear above "University of Birmingham".
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Work Experience item (2015, 2016, Company 1, Intern, Description of job role.) and presses "Save" button.
		#Page should refresh and now list "2015-2016: Company 1, Intern" in Work Experience section, along with all previous content.
		#Page should also read "Description of job role." below this.
		experience_form = self.browser.find_element_by_id("id_experience_form")
		experience_input_start_year_box = experience_form.find_element_by_id("id_experience_input_start_year")
		experience_input_start_year_box.send_keys("2015")
		experience_input_end_year_box = experience_form.find_element_by_id("id_experience_input_end_year")
		experience_input_end_year_box.send_keys("2016")
		experience_input_company_box = experience_form.find_element_by_id("id_experience_input_company")
		experience_input_company_box.send_keys("Company 1")
		experience_input_role_box = experience_form.find_element_by_id("id_experience_input_role")
		experience_input_role_box.send_keys("Intern")
		experience_input_text_box = experience_form.find_element_by_id("id_experience_input_text")
		experience_input_text_box.send_keys("Description of job role.")
		experience_save_button = experience_form.find_element_by_tag_name("button")
		experience_save_button.click()
		time.sleep(1)
		
		experience_item_1 = {"header": "2015-2016: Company 1, Intern", "text": "Description of job role."}
		self.check_for_experience_items_in_order([experience_item_1])
		
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Work Experience item (2018, 2018, Company 2, Intern, Description of job role.) and presses "Save" button.
		#Page should refresh and now list "2018: Company 2, Intern" in Work Experience section, along with all previous content.
		#Page should also read "Description of job role." below this.
		experience_form = self.browser.find_element_by_id("id_experience_form")
		experience_input_start_year_box = experience_form.find_element_by_id("id_experience_input_start_year")
		experience_input_start_year_box.send_keys("2018")
		experience_input_end_year_box = experience_form.find_element_by_id("id_experience_input_end_year")
		experience_input_end_year_box.send_keys("2018")
		experience_input_company_box = experience_form.find_element_by_id("id_experience_input_company")
		experience_input_company_box.send_keys("Company 2")
		experience_input_role_box = experience_form.find_element_by_id("id_experience_input_role")
		experience_input_role_box.send_keys("Intern")
		experience_input_text_box = experience_form.find_element_by_id("id_experience_input_text")
		experience_input_text_box.send_keys("Description of job role.")
		experience_save_button = experience_form.find_element_by_tag_name("button")
		experience_save_button.click()
		time.sleep(1)
		
		experience_item_2 = {"header": "2018: Company 2, Intern", "text": "Description of job role."}
		#Due to start year, "Company 2" should appear above "Company 1".
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Voluntary Experience item (2011, 2012, Company 3, Volunteer, Description of role.) and presses "Save" button.
		#Page should refresh and now list "2011-2012: Company 3, Volunteer" in Voluntary Experience section, along with all previous content.
		#Page should also read "Description of role." below this.
		volunteering_form = self.browser.find_element_by_id("id_volunteering_form")
		volunteering_input_start_year_box = volunteering_form.find_element_by_id("id_volunteering_input_start_year")
		volunteering_input_start_year_box.send_keys("2011")
		volunteering_input_end_year_box = volunteering_form.find_element_by_id("id_volunteering_input_end_year")
		volunteering_input_end_year_box.send_keys("2012")
		volunteering_input_company_box = volunteering_form.find_element_by_id("id_volunteering_input_company")
		volunteering_input_company_box.send_keys("Company 3")
		volunteering_input_role_box = volunteering_form.find_element_by_id("id_volunteering_input_role")
		volunteering_input_role_box.send_keys("Volunteer")
		volunteering_input_text_box = volunteering_form.find_element_by_id("id_volunteering_input_text")
		volunteering_input_text_box.send_keys("Description of role.")
		volunteering_save_button = volunteering_form.find_element_by_tag_name("button")
		volunteering_save_button.click()
		time.sleep(1)
		
		volunteering_item_1 = {"header": "2011-2012: Company 3, Volunteer", "text": "Description of role."}
		self.check_for_volunteering_items_in_order([volunteering_item_1])
		
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Voluntary Experience item (2017, 2017, Company 4, Volunteer, Description of role.) and presses "Save" button.
		#Page should refresh and now list "2017: Company 4, Volunteer" in Voluntary Experience section, along with all previous content.
		#Page should also read "Description of role." below this.
		volunteering_form = self.browser.find_element_by_id("id_volunteering_form")
		volunteering_input_start_year_box = volunteering_form.find_element_by_id("id_volunteering_input_start_year")
		volunteering_input_start_year_box.send_keys("2017")
		volunteering_input_end_year_box = volunteering_form.find_element_by_id("id_volunteering_input_end_year")
		volunteering_input_end_year_box.send_keys("2017")
		volunteering_input_company_box = volunteering_form.find_element_by_id("id_volunteering_input_company")
		volunteering_input_company_box.send_keys("Company 4")
		volunteering_input_role_box = volunteering_form.find_element_by_id("id_volunteering_input_role")
		volunteering_input_role_box.send_keys("Volunteer")
		volunteering_input_text_box = volunteering_form.find_element_by_id("id_volunteering_input_text")
		volunteering_input_text_box.send_keys("Description of role.")
		volunteering_save_button = volunteering_form.find_element_by_tag_name("button")
		volunteering_save_button.click()
		time.sleep(1)
		
		volunteering_item_2 = {"header": "2017: Company 4, Volunteer", "text": "Description of role."}
		#Due to start year, "Company 4" should appear above "Company 3".
		self.check_for_volunteering_items_in_order([volunteering_item_2, volunteering_item_1])
		
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Additional Projects and Achievements item, "I did a thing." and presses "Save" button.
		#Page should refresh and now list "I did a thing." in Additional Projects and Achievements section, along with all previous content.
		projects_form = self.browser.find_element_by_id("id_projects_form")
		projects_input_text_box = projects_form.find_element_by_id("id_projects_input_text")
		projects_input_text_box.send_keys("I did a thing.")
		projects_save_button = projects_form.find_element_by_tag_name("button")
		projects_save_button.click()
		time.sleep(1)
		
		self.check_for_projects(["I did a thing."])
		
		self.check_for_volunteering_items_in_order([volunteering_item_2, volunteering_item_1])
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Additional Projects and Achievements item, "I also did another thing." and presses "Save" button.
		#Page should refresh and now list "I also did another thing." in Additional Projects and Achievements section, along with all previous content.
		projects_form = self.browser.find_element_by_id("id_projects_form")
		projects_input_text_box = projects_form.find_element_by_id("id_projects_input_text")
		projects_input_text_box.send_keys("I also did another thing.")
		projects_save_button = projects_form.find_element_by_tag_name("button")
		projects_save_button.click()
		time.sleep(1)
		
		self.check_for_projects(["I did a thing.", "I also did another thing."])
		
		self.check_for_volunteering_items_in_order([volunteering_item_2, volunteering_item_1])
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Additional Activites, Skills and Hobbies item, "I can do stuff." and presses "Save" button.
		#Page should refresh and now list "I can do stuff." in Additional Activites, Skills and Hobbies section, along with all previous content.
		hobbies_form = self.browser.find_element_by_id("id_hobbies_form")
		hobbies_input_text_box = hobbies_form.find_element_by_id("id_hobbies_input_text")
		hobbies_input_text_box.send_keys("I can do stuff.")
		hobbies_save_button = hobbies_form.find_element_by_tag_name("button")
		hobbies_save_button.click()
		time.sleep(1)
		
		self.check_for_hobbies(["I can do stuff."])
		
		self.check_for_projects(["I did a thing.", "I also did another thing."])
		self.check_for_volunteering_items_in_order([volunteering_item_2, volunteering_item_1])
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new Additional Activities, Skills and Hobbies item, "I can also do things." and presses "Save" button.
		#Page should refresh and now list "I can also do things." in Additional Activities, Skills and Hobbies section, along with all previous content.
		hobbies_form = self.browser.find_element_by_id("id_hobbies_form")
		hobbies_input_text_box = hobbies_form.find_element_by_id("id_hobbies_input_text")
		hobbies_input_text_box.send_keys("I can also do things.")
		hobbies_save_button = hobbies_form.find_element_by_tag_name("button")
		hobbies_save_button.click()
		time.sleep(1)
		
		self.check_for_hobbies(["I can do stuff.", "I can also do things."])
		
		self.check_for_projects(["I did a thing.", "I also did another thing."])
		self.check_for_volunteering_items_in_order([volunteering_item_2, volunteering_item_1])
		self.check_for_experience_items_in_order([experience_item_2, experience_item_1])
		self.check_for_education_items_in_order([education_item_2, education_item_1])
		self.check_for_key_skills(["Programming Skills", "Time Management"])
		self.check_headers()
		self.check_forms()
		self.check_placeholder_reference_text()
		
		#User enters new References item (Person 1, Academic Tutor, 00000 000000, person@email,com) and presses "Save" button.
		#Page should refresh and now list "Person 1, Academic Tutor. Phone: 00000 000000, Email: person@email.com" in References section,
		#along with all previous content except for "References are available on request.", which should no longer be displayed.
		self.fail("Finish writing tests!")
		
		#User enters new References item (Person 2, Work Experience Supervisor, (NO PHONE), (NO EMAIL)) and presses "Save" button.
		#Page should refresh and now list "Person 2, Work Experience Supervisor." in References section, along with all previous content.
		
		#User navigates to CV page again.
		#All previous content should still be there.
		
		#User exits browser, concluding test.
	
