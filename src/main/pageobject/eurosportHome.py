import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
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
        self.ignored_exceptions = (StaleElementReferenceException, ElementClickInterceptedException,)
        WebDriverWait(driver.instance, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                             self.config.get(self.section,
                                                                                             'eurosport_header'))))

    def click_motorsports(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.config.get(self.section, 'motorsports_link'))))
        element.click()

    def click_hamburger(self, exceptions_lst):
        my_element_id = self.config.get(self.section, 'dropdown_button')
        for num in range (2):
            print('Trying clicking in dropdown_button in %s #%d' % (self.click_motorsports_in_dropdown_menu.__name__, num))
            element = WebDriverWait(self.driver, 10, ignored_exceptions=exceptions_lst).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, my_element_id)))
            self.driver.execute_script("arguments[0].click();", element)

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=exceptions_lst).until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.modalnav__rightcol-container.sports-list >div.list-container.tablet')))
                break
            except TimeoutException:
                print('dropdown_button didn\'t work' )

        WebDriverWait(self.driver, 10, ignored_exceptions=exceptions_lst).until(expected_conditions.visibility_of_element_located((By.ID, 'modal_navallsport')))

    def click_motorsports_in_dropdown_menu(self):
        my_element_id2 = self.config.get(self.section, 'popular_sports_motosports_link')

        self.click_hamburger(self.ignored_exceptions)

        for num in range(2):
            print('Trying clicking in motorsports popular sports link in %s #%d' % (self.click_motorsports_in_dropdown_menu.__name__, num))
            link = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).\
                until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, my_element_id2)))
            self.driver.execute_script("arguments[0].click();", link)

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions). \
                    until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, my_element_id2)))
                break
            except TimeoutException:
                print('motorsports link didn\'t work')
        else:
            raise Exception

    def click_motorsports_in_dropdown_menu_right(self):
        my_element_id2 = self.config.get(self.section, 'all_sports_motorsport_link')

        self.click_hamburger(self.ignored_exceptions)

        for num in range(2):
            print('Trying clicking in motorsports all sports link in %s #%d' % (self.click_motorsports_in_dropdown_menu.__name__, num))
            link = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).\
                until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, my_element_id2)))
            self.driver.execute_script("arguments[0].click();", link)

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions). \
                    until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, my_element_id2)))
                break
            except TimeoutException:
                print('motorsports link didn\'t work')

        else:
            raise Exception

    def click_golf(self):
        self.click_hamburger(self.ignored_exceptions)
        my_element_id2 = self.config.get(self.section, 'popular_sports_golf_link')

        for num in range(2):
            print('Trying clicking in golf link in %s #%d' % (self.click_motorsports_in_dropdown_menu.__name__, num))
            link = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).\
                until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, my_element_id2)))
            self.driver.execute_script("arguments[0].click();", link)

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions). \
                    until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, my_element_id2)))
                break
            except TimeoutException:
                print('golf link didn\'t work')

        else:
            raise Exception