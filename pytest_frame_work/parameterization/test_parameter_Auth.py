import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
@pytest.mark.parametrize("username,password",[("Admi","admin123"),("Admin","admin123"),("add","added")])
def test_login(username,password):
    serv_obj = Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    b = driver.find_element(By.XPATH, "//button[normalize-space()='Upgrade']").is_displayed()
    try:
        assert b==True
        driver.close()
    except:
        assert b==False
        driver.close()
