import unittest
from src.main.common.driver import Driver
from src.main.common import utils
from src.main.pageobject.eurosportHome import HomeScreen
from src.main.pageobject.eurosportMotorsports import MotorsportScreen
from src.main.pageobject.eurosportMotorcycling import MotorcyclingScreen
from src.main.pageobject.eurosportGolf import GolfScreen
from src.main.configs.config import Config


class eurosportMotorsport(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver('eurosport_selectors')
        cls.config_obj = Config()
        cls.driver.navigate(cls.config_obj.config.get('URLs', 'eurosport_base_url'))
        utils.accept_privacy(cls.driver, cls.config_obj.config)

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

        motorcycling_screen = MotorcyclingScreen(self.driver, self.config_obj.config)
        motorcycling_screen.click_standings()
        motorcycling_screen.click_motogp_standings()
        motorcycling_screen.click_miguel()

#    @unittest.skip('')
    def test_insert_comment_article_golf(self):
        self.homepage.click_golf()
        golf_screen = GolfScreen(self.driver, self.config_obj.config)
        article_name = golf_screen.click_first_article().split('\n')[0]
        assert golf_screen.get_article_title() == article_name
        assert golf_screen.get_article_publisher()


    def tearDown(self):
        self.take_snapshot_if_failure()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

    def take_snapshot_if_failure(self):
        for method, error in self._outcome.errors:
            if error:
                self.driver.instance.save_screenshot('/var/tmp/screenshot%s.png' % self.id())


if __name__ == "__main__":
    unittest.main()