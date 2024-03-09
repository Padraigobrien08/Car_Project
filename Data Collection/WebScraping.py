
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.common.by as By

# create a Service object for the chromedriver executable
service = Service(executable_path=r"C:\Users\Padraig\Desktop\Car_Project\chromedriver-win64\chromedriver.exe")
# create a new Chrome session
driver = webdriver.Chrome(service=service)
val = "https://www.donedeal.ie/cars"
wait = WebDriverWait(driver, 10)
driver.get(val)

get_url = driver.current_url
wait.until(EC.url_to_be(val))
# find the element by its Xpath
element = driver.find_element(By.By.XPATH, "//div[@id='BasicHeaderstyled__Title-sc-78ow8b-0 cGWGnJ']")

# get the HTML source of the element
element_source = element.get_attribute("innerHTML")

driver.quit()
