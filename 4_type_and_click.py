from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Start Chrome
driver = webdriver.Chrome()


# Open Python website
driver.get("https://www.python.org")


# Give the website time to load
time.sleep(3)


# Find the search box
search_box = driver.find_element(
    By.ID,
    "id-search-field"
)


# Type Django
search_box.send_keys("Django")


# Keep browser open so we can see the result
time.sleep(5)