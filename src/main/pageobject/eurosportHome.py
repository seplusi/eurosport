import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
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
        WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id))).click()

        my_element_id2 = self.config.get(self.section, 'popular_sports_motosports_link')
        WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id2))).click()

    def click_motorsports_in_dropdown_menu_right(self):
        ignored_exceptions = (StaleElementReferenceException,)

        my_element_id = self.config.get(self.section, 'dropdown_button')
        WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).\
                until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id))).click()

        my_element_id = self.config.get(self.section, 'all_sports_motorsport_link')
        element = WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).\
                until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, my_element_id)))
        print(element.text)
        element.click()