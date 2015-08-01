from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		inputbox = self.get_item_input_box()
		#Edith goes to the home page and accidentally tries to submit
		#an empty list item. She hits Enter
		self.browser.get(self.server_url)
		inputbox.send_keys('\n')
		
		#The home page refreshes. There is an error message
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")
		
		#She tries again with some text, which works
		inputbox.send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')
		
		#Blank again, which again 
		inputbox.send_keys('\n')
		
		#gives a warning message
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")
		
		#She corrects it by filling in some text
		inputbox.send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')
		
		
