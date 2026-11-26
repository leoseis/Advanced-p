from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

# Open Python website
driver.get("https://www.python.org")

search_box = driver.find_element(
    By.ID,
    "id-search-field"
)