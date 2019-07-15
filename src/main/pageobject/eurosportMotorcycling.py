class MotorcyclingScreen:

    def __init__(self, driver, config):
        self.driver = driver.instance
        self.config = config
        self.section = driver.section

        self.standings_link = self.driver.find_element_by_css_selector(self.config.get(self.section, 'motogp_standings_link'))

    def click_standings(self):
        self.standings_link.click()

    def click_motogp_standings(self):
        elements = self.driver.find_elements_by_css_selector(self.config.get(self.section, 'motogp_cat_link'))
        for element in elements:
            if element.text == 'MotoGP':
                break
        element.click()

    def click_miguel(self):
        self.driver.find_element_by_css_selector(self.config.get(self.section, 'miguel_gc_position_link')).click()
        self.driver.find_element_by_css_selector(self.config.get(self.section, 'miguel_profile'))


