import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from src.main.common.driver import Driver
from src.main.pageobject.eurosportHome import HomeScreen
from src.main.pageobject.eurosportMotorsports import MotorsportScreen


class eurosportMotorsport(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate("https://www.eurosport.co.uk")

    def test_motorsports_in_main_menu(self):
        HomeScreen(self.driver).click_motorsports()
        MotorsportScreen(self.driver)
        pass

    @unittest.skip('')
    def test_motorsports_in_dropdown_menu(self):
        pass

    @unittest.skip('')
    def test_motorsports_in_dropdown_menu2(self):
        pass

    @unittest.skip('')
    def test_find_miguel_oliveira(self):
        pass

    def tearDown(self):
        self.driver.instance.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()