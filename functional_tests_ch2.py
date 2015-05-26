from selenium import webdriver

browser = webdriver.Firefox()

#Open up the app
browser.get('http://localhost:8000')

#Test that title contains "To-Do"
assert 'To-Do' in browser.title, "Browser title was " + browser.title

#Enter a to-do list item (through an input box)

#Type in "Buy peacock feathers" into the input box

#Make sure that that appears in the first row of the table

#Then, add another item "Use peacock feathers to make a fly"

browser.quit()