from selenium.common.exceptions import StaleElementReferenceException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class GolfScreen:

    def __init__(self, driver, config):
        self.driver = driver.instance
        self.config = config
        self.section = driver.section
        self.ignored_exceptions = (StaleElementReferenceException, )

        WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              self.config.get(self.section,
                                                              'golf_text_in_motorsport_page'))))

    def click_first_article(self):
        for num in range(2):
            print('Trying clicking in golf article in %s #%d' % (self.click_first_article.__name__, num))
            element = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                  self.config.get(self.section, 'golf_latest_news'))))[0]
            article_text = element.text
            self.driver.execute_script("arguments[0].click();", element)

            try:
                WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.tab-content.active.storylist-latest-content > div.storylist-container-latest')))
                break
            except TimeoutException:
                print('dropdown_button didn\'t work')

        return article_text

    def get_article_title(self):
        return WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(EC.element_to_be_clickable((By.CLASS_NAME,self.config.get(self.section, 'golf_article_title')))).text

    def get_article_publisher(self):
        return WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions).until(
            EC.visibility_of_element_located((By.CLASS_NAME,
                                                   self.config.get(self.section, 'golf_article_publisher')))).is_displayed()