class MotorsportScreen:

    def __init__(self, driver):
        self.driver = driver

        self.driver.instance.find_element_by_css_selector('li[class^="bread"] > a[href^="/allmotor"]')
        self.driver.instance.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.instance.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')
        self.motogp_link = self.driver.instance.find_element_by_css_selector('li[class="categorylist__item"] > a[href="/moto/"]')

    def click_motogp(self):
        self.motogp_link.click()
