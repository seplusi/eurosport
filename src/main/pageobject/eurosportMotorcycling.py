class MotorcyclingScreen:

    def __init__(self, driver):
        self.driver = driver
        self.standings_link = self.driver.instance.find_element_by_css_selector('ul[class="categorylist"] > li > a[href^="/moto/world-championship/standing"]')

    def click_standings(self):
        self.standings_link.click()

    def click_motogp_standings(self):
        elements = self.driver.instance.find_elements_by_css_selector('div[id^="standings-tabs"] span[class="navtab-label"]')
        for element in elements:
            if element.text == 'MotoGP':
                break
        element.click()

    def click_miguel(self):
        self.driver.instance.find_element_by_css_selector('a[href^="/moto/miguel"]').click()
        self.driver.instance.find_element_by_css_selector('h1[class="person-head__person-name"]')


