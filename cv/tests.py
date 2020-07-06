from django.test import TestCase
from django.urls import resolve
from cv.views import cv

# Create your tests here.

class CVPageTest(TestCase):
	
	def test_cv_url_resolves_to_correct_view(self):
		found = resolve("/cv/")
		self.assertEqual(found.func, cv)