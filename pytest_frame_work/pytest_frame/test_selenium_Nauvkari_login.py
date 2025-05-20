from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")

# Explicit wait for the login button to be clickable
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@id='login_Layer']"))
)
login_button.click()

# Explicit wait for the email input field to be present
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter your active Email ID / Username']"))
)
email_input.send_keys("venkatakrishnababuchunduru@gmail.com")