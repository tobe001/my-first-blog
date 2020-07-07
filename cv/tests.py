from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from cv.views import cv

# Create your tests here.

class CVPageTest(TestCase):
	
	def test_cv_url_resolves_to_correct_view(self):
		found = resolve("/cv/")
		self.assertEqual(found.func, cv)
	
	def test_page_returns_correct_html(self):
		request = HttpRequest()
		response = cv(request)
		html = response.content.decode("utf8")
		self.assertTrue(html.startswith("<html>"))
		self.assertIn("<title>My CV</title>", html)
		self.assertTrue(html.endswith("</html>"))