from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MotorsportScreen:

    def __init__(self, driver, config):
        self.driver = driver.instance
        self.config = config
        self.section = driver.section

        WebDriverWait(driver.instance, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                             self.config.get(self.section,
                                                                                             'motorsports_text_in_motorsport_page'))))

    def click_motogp(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.config.get(self.section, 'motogp_link'))))
        element.click()
