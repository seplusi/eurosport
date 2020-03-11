from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MotorcyclingScreen:

    def __init__(self, driver, config):
        self.driver = driver.instance
        self.config = config
        self.section = driver.section

#        self.standings_link = self.driver.find_element_by_css_selector(self.config.get(self.section, 'motogp_standings_link'))
        self.get_standings_element()

    def get_standings_element(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                   self.config.get(self.section,
                                                                                                   'motogp_standings_link'))))

    def click_standings(self):
        self.get_standings_element().click()

    def click_motogp_standings(self):
#        elements = self.driver.find_elements_by_css_selector(self.config.get(self.section, 'motogp_cat_link'))
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                                   self.config.get(self.section,
                                                                                                   'motogp_cat_link'))))
        for element in elements:
            if element.text == 'MotoGP':
                break
        element.click()

    def click_miguel(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                               self.config.get(self.section,
                                                                                               'miguel_gc_position_link')))).click()
#        self.driver.find_element_by_css_selector(self.config.get(self.section, 'miguel_gc_position_link')).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                               self.config.get(self.section,
                                                                                               'miguel_profile'))))
#        self.driver.find_element_by_css_selector(self.config.get(self.section, 'miguel_profile'))


