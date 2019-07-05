class HomeScreen:

    def __init__(self, driver):
        self.driver = driver.instance
        self.motorsports_link = self.driver.find_element_by_css_selector('li[class^="category"] > a[href^="/allmotorsports"]')

    def click_motorsports(self):
        self.motorsports_link.click()