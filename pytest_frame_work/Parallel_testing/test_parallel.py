#import pytest
import time

from selenium   import webdriver
from selenium.webdriver.common.by import By
class Test_title:
    def test_chrome_title(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj=Service(r"D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get('https://msys.keka.com/#/me/attendance/logs')
        time.sleep(4)
        print(self.driver.title)
    def test_edge_title(self):
        from selenium.webdriver.edge.webdriver import Service
        self.serv_obj=Service(r"D:\Downloads\edgedriver_win64\msedgedriver.exe")
        self.driver=webdriver.Edge(service=self.serv_obj)
        self.driver.get('https://www.jqueryscript.net/slider/')
        print(self.driver.title)