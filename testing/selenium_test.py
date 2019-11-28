from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")

assert "Google" in driver.title

elem = driver.find_element_by_name("q")

elem.send_keys("python")
# elem.clear()
elem.send_keys(Keys.RETURN)
assert "Welcome to Python" in driver.page_source

elem = driver.find_element_by_partial_link_text("Welcome to Python")
elem.click()
print(driver.title)  # Welcome to Python.org
print(driver.current_url)  # https://www.python.org/
elem = driver.find_element_by_id('news')
elem.click()

driver.close()
