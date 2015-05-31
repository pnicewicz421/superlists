from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import test
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Open webpage
		self.browser.get('http://localhost:8000')
		
		#"To-Do" in title and header
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		
		#Make sure that inputbox 'placeholder' attribute is equal to "Enter a to-do item"
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		#Enter "buy peacock feathers" to the input field and send
		inputbox.send_keys("Buy peacock feathers")
		inputbox.send_keys(Keys.ENTER)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys("Use peacock feathers to make a fly")
		inputbox.send_keys(Keys.ENTER)
		
		#After a refresh, make sure that that input now appears in the row in the table
		table = self.browser.find_element_by_id('id_list_table')
		rows = self.browser.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn('2: Use peacock feathers to make fly', [row.text for row in rows])
		
		self.fail('Finish the test!')
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')