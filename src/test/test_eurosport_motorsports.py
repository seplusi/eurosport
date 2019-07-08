import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from src.main.common.driver import Driver
from src.main.pageobject.eurosportHome import HomeScreen
from src.main.pageobject.eurosportMotorsports import MotorsportScreen
from src.main.pageobject.eurosportMotorcycling import MotorcyclingScreen


class eurosportMotorsport(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver()

    def setUp(self):
        self.driver.navigate("https://www.eurosport.co.uk")
        self.homepage = HomeScreen(self.driver)

#    @unittest.skip('')
    def test_motorsports_in_main_menu(self):
        self.homepage.click_motorsports()
        MotorsportScreen(self.driver)

#    @unittest.skip('')
    def test_motorsports_in_dropdown_menu(self):
        self.homepage.click_motorsports_in_dropdown_menu()
        MotorsportScreen(self.driver)

#    @unittest.skip('')
    def test_motorsports_in_dropdown_menu2(self):
        self.homepage.click_motorsports_in_dropdown_menu_right()
        MotorsportScreen(self.driver)

#    @unittest.skip('')
    def test_find_miguel_oliveira(self):
        self.homepage.click_motorsports_in_dropdown_menu()
        MotorsportScreen(self.driver).click_motogp()
        MotorcyclingScreen(self.driver).click_standings()
        MotorcyclingScreen(self.driver).click_motogp_standings()
        MotorcyclingScreen(self.driver).click_miguel()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()