import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomeScreen:

    def __init__(self, driver, config):
        self.driver = driver.instance
        self.config = config
        self.section = driver.section
        WebDriverWait(driver.instance, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             self.config.get(self.section,
                                                                                             'eurosport_header'))))

    def click_motorsports(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.config.get(self.section, 'motorsports_link'))))
        element.click()

    def click_motorsports_in_dropdown_menu(self):
        ignored_exceptions = (StaleElementReferenceException,)

        my_element_id = self.config.get(self.section, 'dropdown_button')
        my_element_id2 = self.config.get(self.section, 'popular_sports_motosports_link')
        for num in range (2):
            print('Trying clicking in dropdown_button in %s #%d' % (self.click_motorsports_in_dropdown_menu.__name__, num))
            WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id))).click()

     #       while True:
     #           if self.driver.find_elements_by_css_selector(
     #               'div.modalnav__rightcol-container.sports-list >div.list-container.tablet')[0].size['height'] != 0:
     #               break
            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=()).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.modalnav__rightcol-container.sports-list >div.list-container.tablet')))
                break
            except TimeoutException:
                print('dropdown_button didn\'t work' )

        for num in range(2):
            print('Trying clicking in motorsports link in %s #%d' % (self.click_motorsports_in_dropdown_menu.__name__, num))
            WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).\
                until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id2))).click()

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions). \
                    until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, my_element_id2)))
                break
            except TimeoutException:
                print('motorsports link didn\'t work')

    def click_motorsports_in_dropdown_menu_right(self):
        ignored_exceptions = (StaleElementReferenceException,)
        my_element_id = self.config.get(self.section, 'dropdown_button')
        my_element_id2 = self.config.get(self.section, 'all_sports_motorsport_link')

        for num in range(2):
            print('Trying clicking in dropdown_button in %s #%d' % (self.click_motorsports_in_dropdown_menu_right.__name__, num))
            WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).\
                    until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id))).click()

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.modalnav__rightcol-container.sports-list >div.list-container.tablet')))
                break
            except TimeoutException:
                print('dropdown_button didn\'t work' )


        WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).\
                until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id2))).click()
