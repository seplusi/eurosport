from selenium.common.exceptions import NoSuchElementException
import time


class HomeScreen:

    def __init__(self, driver, config):
        self.driver = driver.instance
        self.config = config
        self.section = driver.section
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_css_selector(self.config.get(self.section, 'popup_close_cross')).click()
        except NoSuchElementException:
            print('No popup. No need to accetp.')
        finally:
            self.driver.implicitly_wait(60)

        self.motorsports_link = self.driver.find_element_by_css_selector(self.config.get(self.section, 'motorsports_link'))
        self.motorsports_link = self.driver.find_element_by_css_selector(self.config.get(self.section, 'motorsports_link'))

    def click_motorsports(self):
        self.motorsports_link.click()

    def click_motorsports_in_dropdown_menu(self):
        self.driver.find_element_by_css_selector(self.config.get(self.section, 'dropdown_button')).click()
        for _ in range(10):
            var = self.driver.find_element_by_css_selector(self.config.get(self.section, 'popular_sports_motosports_link'))
            if var.text == 'Motorsports':
                var.click()
                break
            else:
                time.sleep(1)
                print('Slept a bit')
        else:
            self.assertTrue(False)

    def click_motorsports_in_dropdown_menu_right(self):
        self.driver.find_element_by_css_selector(self.config.get(self.section, 'dropdown_button')).click()
        for _ in range(10):
            var = self.driver.find_element_by_css_selector(self.config.get(self.section, 'all_sports_motorsport_link'))
            if var.text == 'Motorsports':
                var.click()
                break
            else:
                time.sleep(1)
                print('Slept a bit')
        else:
            self.assertTrue(False)
