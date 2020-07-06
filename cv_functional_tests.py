from selenium import webdriver
import unittest

class CVTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()
	
	def test_fill_cv_and_retrieve(self):
		
		#User navigates to site's CV page.
		#Page title should mention the CV.
		self.browser.get("http://127.0.0.1:8000/cv")
		self.assertIn("CV", self.browser.title)
		self.fail("Finish writing tests!")
		
		#Page should include my name.
		
		#Page should contain appropriate section headers:
		#Profile
		#Key Skills
		#Education
		#Work Experience
		#Voluntary Experience
		#Additional Projects and Achievements
		#Additional Activities, Skills and Hobbies
		#References
		
		#Page should contain input boxes for:
		#Key Skills (Text)
		#Education (Start Year, End Year, Institution, Course Title, Text)
		#Work Experience (Start Year, End Year, Company, Role, Text)
		#Voluntary Experience (Start Year, End Year, Company, Role, Text)
		#Additional Projects and Achievements (Text)
		#Additional Activities, Skills and Hobbies (Text)
		#References (Name, Relevance, Phone, Email)
		
		#In the absence of any references, the References section should read "References available on request."
		
		#User enters new Key Skill, "Programming Skills" and hits enter.
		#Page should refresh and now list "Programming Skills" in the Key Skills section, along with all previous content.
		
		#User enters new Key Skill, "Time Management" and hits enter.
		#Page should refresh and now list "Time Management" in the Key Skills section, along with all previous content.
		
		#User enters new Education Item (2018, 2022, University of Birmingham, MSci Mathematics and Computer Science, Description of course and results.) and hits enter.
		#Page should refresh and now list "2018-2022: University of Birmingham, MSci Mathematics and Computer Science" in Education section, along with all previous content.
		#Page should also read "Description of course and results." below this.
		
		#User enters new Eductaion Item (2020, 2020, Abnormal School, (NO COURSE TITLE), Description of course and results.) and hits enter.
		#Page should now refresh and list "2020: Abnormal School" in Education section, along with all previous content.
		#Page should also read "Description of course and results." below this.
		
		#Due to start year, "Abnormal School" should appear above "University of Birmingham".
		
		#User enters new Work Experience item (2015, 2016, Company 1, Intern, Description of job role.) and hits enter.
		#Page should refresh and now list "2015-2016: Company 1, Intern" in Work Experience section, along with all previous content.
		#Page should also read "Description of job role." below this.
		
		#User enters new Work Experience item (2018, 2018, Company 2, Intern, Description of job role.) and hits enter.
		#Page should refresh and now list "2018: Company 2, Intern" in Work Experience section, along with all previous content.
		#Page should also read "Description of job role." below this.
		
		#Due to start year, "Company 2" should appear above "Company 1".
		
		#User enters new Voluntary Experience item (2011, 2012, Company 3, Volunteer, Description of role.) and hits enter.
		#Page should refresh and now list "2011-2012: Company 3, Volunteer" in Voluntary Experience section, along with all previous content.
		#Page should also read "Description of role." below this.
		
		#User enters new Voluntary Experience item (2017, 2017, Company 4, Volunteer, Description of role.) and hits enter.
		#Page should refresh and now list "2017: Company 4, Volunteer" in Voluntary Experience section, along with all previous content.
		#Page should also read "Description of role." below this.
		
		#Due to start year, "Company 4" should appear above "Company 3".
		
		#User enters new Additional Projects and Achievements item, "I did a thing." and hits enter.
		#Page should refresh and now list "I did a thing." in Additional Projects and Achievements section, along with all previous content.
		
		#User enters new Additional Projects and Achievements item, "I also did another thing." and hits enter.
		#Page should refresh and now list "I also did another thing." in Additional Projects and Achievements section, along with all previous content.
		
		#User enters new Additional Activites, Skills and Hobbies item, "I can do stuff." and hits enter.
		#Page should refresh and now list "I can do stuff." in Additional Activites, Skills and Hobbies section, along with all previous content.
		
		#User enters new Additional Activities, Skills and Hobbies item, "I can also do things." and hits enter.
		#Page should refresh and now list "I can also do things." in Additional Activities, Skills and Hobbies section, along with all previous content.
		
		#User enters new References item (Person 1, Academic Tutor, 00000 000000, person@email,com) and hits enter.
		#Page should refresh and now list "Person 1, Academic Tutor. Phone: 00000 000000, Email: person@email.com" in References section,
		#along with all previous content except for "References are available on request.", which should no longer be displayed.
		
		#User enters new References item (Person 2, Work Experience Supervisor, (NO PHONE), (NO EMAIL)) and hits enter.
		#Page should refresh and now list "Person 2, Work Experience Supervisor." in References section, along with all previous content.
		
		#User navigates to CV page again.
		#All previous content should still be there.
		
		#User exits browser, concluding test.
	

if __name__ == "__main__":
	unittest.main(warnings = "ignore")