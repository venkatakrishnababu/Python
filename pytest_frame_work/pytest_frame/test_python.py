from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
login_button = driver.find_element(By.XPATH, "//a[@id='login_Layer']")
time.sleep(5)
login_button.click()
time.sleep(5)
email_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your active Email ID / Username']")
email_input.send_keys("venkatakrishnababuchunduru@gmail.com")
time.sleep(2)
email_password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your password']")
email_password.send_keys("R@hul999")
time.sleep(5)
Click_login = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.loginButton")
Click_login.click()
time.sleep(5)
Click_profile_image = driver.find_element(By.CLASS_NAME, "nI-gNb-icon-img")
Click_profile_image.click()
time.sleep(5)
logout_link = driver.find_element(By.CSS_SELECTOR, "a[title='Logout']")
logout_link.click()
time.sleep(10)



    #assert "Jobs - Recruitment - Job Search - Employment - Job Vacancies - Naukri.com" in driver.title, "Title mismatch"  # Example title
driver.quit()

