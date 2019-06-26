import unittest
import time
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

        # driver = webdriver.Chrome(chrome_options=options)

        # create a new Firefox session
        self.driver = webdriver.Chrome(executable_path="/home/luis/Programs/chromedriver/chromedriver", options=options)
        self.driver.implicitly_wait(30)

        # Navigate to the application home page and get rid of the popup
        self.driver.get("https://www.eurosport.co.uk")
        elements = self.driver.find_elements_by_css_selector('div > button[class="qc-cmp-button"]')
        self.assertTrue(len(elements) == 1, 'ERROR: %s' % str([x.text for x in elements]))
        elements[0].click()
        print('Hello World')

    def test_motorsports_in_main_menu(self):
        self.driver.find_element_by_css_selector('li[class^="category"] > a[href^="/allmotor"]').click()
        self.driver.find_element_by_css_selector('li[class^="bread"] > a[href^="/allmotor"]')
        self.driver.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')

    def test_motorsports_in_dropdown_menu(self):
        self.driver.find_element_by_css_selector('button[class="hamburger"] > span').click()
        self.driver.find_element_by_css_selector('div[class="overflower"]> ul[class="popular-nav"]  a[href^="/allmotor"]').click()
        self.driver.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()