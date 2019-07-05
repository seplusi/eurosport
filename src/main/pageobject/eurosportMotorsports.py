class MotorsportScreen:

    def __init__(self, driver):
        self.driver = driver.instance

        self.driver.find_element_by_css_selector('li[class^="bread"] > a[href^="/allmotor"]')
        self.driver.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')
