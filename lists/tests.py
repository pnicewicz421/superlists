from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class homePageTest(TestCase):
	
	def test_root_url_resolvers_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
		
	def test_home_page_returns_correct_html(self):		
		request = HttpRequest()
		response = home_page(request)
		
		expected_html = render_to_string('home.html')
		#print (response.content.decode())
		self.assertEqual(response.content.decode(), expected_html)
		
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>To-Do lists</title>', response.content)
		#self.assertTrue(response.content.strip().endswith(b'</html>')) 

	def test_home_page_can_save_a_POST_request(self):
		#setup
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'
		
		#exercise
		response = home_page(request)
		
		#assert
		self.assertIn('A new list item', response.content.decode()) 
		expected_html = render_to_string(
			'home.html', 
			{'new_item_text': 'A new list item'}
		)
		#print (response.content.decode())
		self.assertEqual(response.content.decode(), expected_html)

		
		
		
