import unittest
import time

from django.contrib.admin.helpers import checkbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import pytest
driver = webdriver.Chrome(executable_path='../../myvenv/Scripts/chromedriver.exe')

class test_customeredit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_customeredit(self):
        self.driver.get("http://127.0.0.1:8000/login/")
        self.driver.set_window_size(1280, 656)
        self.driver.find_element(By.ID, "id_email").send_keys("anits1088@gmail.com")
        self.driver.find_element(By.ID, "id_password").send_keys("Sampath@3")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "View details » ").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Edit").click()
        self.driver.find_element(By.ID, "id_city").click()
        self.driver.find_element(By.ID, "id_city").send_keys("denver")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".save").click()
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
