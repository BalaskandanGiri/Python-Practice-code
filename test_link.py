from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
driver=webdriver.Firefox(executable_path='C:\\Users\I346330\Downloads\Softwares\geckodriver.exe')
driver.get("http://testlink.ariba.com/")
#assert "Python" in driver.title
driver.implicitly_wait(5)
print(driver.page_source.encode("utf-8"))
#driver.switch_to.frame("topwindow")
elem = driver.find_element_by_name("tl_login")
elem.send_keys("I346330")
elem = driver.find_element_by_name("tl_password")
elem.send_keys("")
elem = driver.find_element_by_name("login_submit")
elem.send_keys(Keys.ENTER)
#driver.implicitly_wait(10)
driver.switch_to.frame("mainframe")
print(driver.page_source.encode("utf-8"))
elem = driver.find_element_by_link_text("Edit Test Cases")
elem.click()
print(driver.page_source.encode('utf-8'))
driver.switch_to.default_content()
driver.switch_to.frame("mainframe")
elem=driver.switch_to.frame("treeframe")
time.sleep(2)
innerHTML = driver.execute_script("return document.documentElement.innerHTML;")
print(innerHTML)
driver.find_element_by_tag_name('img').find_element_by_id("ext-gen24")
elem.click()
'''elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source'''
