from selenium.common.exceptions import NoSuchElementException
import time


class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        try:
            self.driver.instance.implicitly_wait(10)
            self.driver.instance.find_element_by_css_selector('div[class="abtasty-modal__close abtasty-modal__close--inside"]').click()
        except NoSuchElementException:
            print('No popup. No need to accetp.')
        finally:
            self.driver.instance.implicitly_wait(60)

        self.motorsports_link = self.driver.instance.find_element_by_css_selector('li[class^="category"] > a[href^="/allmotorsports"]')

    def click_motorsports(self):
        self.motorsports_link.click()

    def click_motorsports_in_dropdown_menu(self):
        self.driver.instance.find_element_by_css_selector('button[class="hamburger"] > span').click()
        for _ in range(10):
            var = self.driver.instance.find_element_by_css_selector('div[class="overflower"]> ul[class="popular-nav"] > li > a[href="/allmotorsports/"]')
            if var.text == 'Motorsports':
                var.click()
                break
            else:
                time.sleep(1)
                print('Slept a bit')
        else:
            self.assertTrue(False)

    def click_motorsports_in_dropdown_menu_right(self):
        self.driver.instance.find_element_by_css_selector('button[class="hamburger"] > span').click()
        for _ in range(10):
            var = self.driver.instance.find_element_by_css_selector('ul[class="allsports-desktop"] > li > a[href="/allmotorsports/"]')
            if var.text == 'Motorsports':
                var.click()
                break
            else:
                time.sleep(1)
                print('Slept a bit')
        else:
            self.assertTrue(False)
