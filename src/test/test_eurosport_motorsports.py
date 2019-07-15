import unittest
from src.main.common.driver import Driver
from src.main.pageobject.eurosportHome import HomeScreen
from src.main.pageobject.eurosportMotorsports import MotorsportScreen
from src.main.pageobject.eurosportMotorcycling import MotorcyclingScreen
from src.main.configs.config import Config


class eurosportMotorsport(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver('eurosport_selectors')
        cls.config_obj = Config()

    def setUp(self):
        self.driver.navigate(self.config_obj.config.get('URLs', 'eurosport_base_url'))
        self.homepage = HomeScreen(self.driver, self.config_obj.config)

#    @unittest.skip('')
    def test_motorsports_in_main_menu(self):
        self.homepage.click_motorsports()
        MotorsportScreen(self.driver, self.config_obj.config)

#    @unittest.skip('')
    def test_motorsports_in_dropdown_menu(self):
        self.homepage.click_motorsports_in_dropdown_menu()
        MotorsportScreen(self.driver, self.config_obj.config)

#    @unittest.skip('')
    def test_motorsports_in_dropdown_menu2(self):
        self.homepage.click_motorsports_in_dropdown_menu_right()
        MotorsportScreen(self.driver, self.config_obj.config)

#    @unittest.skip('')
    def test_find_miguel_oliveira(self):
        self.homepage.click_motorsports_in_dropdown_menu()
        MotorsportScreen(self.driver, self.config_obj.config).click_motogp()
        MotorcyclingScreen(self.driver, self.config_obj.config).click_standings()
        MotorcyclingScreen(self.driver, self.config_obj.config).click_motogp_standings()
        MotorcyclingScreen(self.driver, self.config_obj.config).click_miguel()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()