from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
	def test_cannot_add_empty_list_items(self):
		#Edith goes to the home page and accidentally tries to submit
		#an empty list item. She hits Enter
		
		#The home page refreshes. There is an error message
		
		#She tries again with some text, which works
		
		#Blank again, which again 
		
		#gives a warning message
		
		#She corrects it by filling in some text
		
		self.fail('write me!')
		
