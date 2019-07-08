import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option('w3c', False)
        options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

        # driver = webdriver.Chrome(chrome_options=options)

        # create a new Firefox session
        cls.driver = webdriver.Chrome(executable_path="/home/luis/Programs/chromedriver/chromedriver", options=options)
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://www.eurosport.co.uk")
        try:
            element = cls.driver.find_element_by_xpath('//button[text()=" I accept "]')
            if cls._link_has_gone_stale(cls, element):
                print('Entry page has gobe stale')

            print('%s %s' % (element.tag_name, element.text))
            element.click()
        except NoSuchElementException:
            print('No popup. No need to accetp.')
        finally:
            cls.driver.implicitly_wait(60)

    def setUp(self):
        self._started_at = time.time()
        self.driver.get("https://www.eurosport.co.uk")

    def _link_has_gone_stale(self, element):
        try:
            # poll the link with an arbitrary call
            self.driver.implicitly_wait(1)
            element.find_elements_by_id('doesnt-matter')
            return False
        except StaleElementReferenceException:
            return True
        finally:
            self.driver.implicitly_wait(60)

    def _check_stale_and_click(self, element):
        if self._link_has_gone_stale(element):
            print('%s % is STALE' %(element.tag_name, element.text))
        element.click()

    def test_motorsports_in_main_menu(self):
        motorsport = self.driver.find_element_by_css_selector('li[class^="category"] > a[href^="/allmotorsports"]')
        self._check_stale_and_click(motorsport)
        self.driver.find_element_by_css_selector('li[class^="bread"] > a[href^="/allmotor"]')
        self.driver.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')

    def test_motorsports_in_dropdown_menu(self):
        self.driver.find_element_by_css_selector('button[class="hamburger"] > span').click()
        motorsport = self.driver.find_element_by_css_selector('div[class="overflower"]> ul[class="popular-nav"]  a[href^="/allmotorsports"]')
        self._check_stale_and_click(motorsport)
        self.driver.find_element_by_css_selector('li[class="breadcrumb-item fade-in two"] > a[href="/allmotorsports/"]')
        self.driver.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')

    def test_motorsports_in_dropdown_menu2(self):
        self.driver.find_element_by_css_selector('button[class="hamburger"] > span').click()
        motorsport = self.driver.find_element_by_css_selector('ul[class="allsports-desktop"] > li > a[href="/allmotorsports/"]')
        self._check_stale_and_click(motorsport)
        self.driver.find_element_by_css_selector('li[class="breadcrumb-item fade-in two"] > a[href="/allmotorsports/"]')
        self.driver.find_element_by_css_selector('div > div[class ="livebox-caption"]')
        self.driver.find_element_by_css_selector('div[id^="navtab-storylist-desk"] a[href="#featured"] > span[class="navtab-label"]')

    def test_find_miguel_oliveira(self):
        self.driver.find_element_by_css_selector('button[class="hamburger"] > span').click()
        motorsport = self.driver.find_element_by_css_selector('ul[class="allsports-desktop"] > li > a[href="/allmotorsports/"]')
        self._check_stale_and_click(motorsport)
        motogp = self.driver.find_element_by_css_selector('li[class="categorylist__item"] > a[href="/moto/"]')
        self._check_stale_and_click(motogp)
        standings = self.driver.find_element_by_css_selector('ul[class="categorylist"] > li > a[href^="/moto/world-championship/standing"]')
        self._check_stale_and_click(standings)
        elements = self.driver.find_elements_by_css_selector('div[id^="standings-tabs"] span[class="navtab-label"]')
        for element in elements:
            if element.text == 'MotoGP':
                break
        self._check_stale_and_click(element)
        name = self.driver.find_element_by_css_selector('a[href^="/moto/miguel"]')
        self._check_stale_and_click(name)
        self.driver.find_elements_by_css_selector('h1[class="person-head__person-name"]')

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()