from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def accept_privacy(driver, config):
    selector = config.get(driver.section, 'accept_gdpr')
    element = WebDriverWait(driver.instance, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
    element.click()