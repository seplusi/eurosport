class MotorsportScreen:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.section = driver.section

        self.driver.instance.find_element_by_css_selector(self.config.get(self.section, 'motorsports_text_in_motorsport_page'))
        self.driver.instance.find_element_by_css_selector(self.config.get(self.section, 'motorsport_all_scores'))
        self.driver.instance.find_element_by_css_selector(self.config.get(self.section, 'motorsport_featured'))
        self.motogp_link = self.driver.instance.find_element_by_css_selector(self.config.get(self.section, 'motogp_link'))

    def click_motogp(self):
        self.motogp_link.click()
