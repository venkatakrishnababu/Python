import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
class Test_login:
    def test_login(self,set_up):
        driver=set_up
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
