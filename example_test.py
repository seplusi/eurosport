from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

#driver = webdriver.Chrome(chrome_options=options)

# create a new Firefox session
driver = webdriver.Chrome(executable_path="/home/luis/Programs/chromedriver/chromedriver", chrome_options=options)
driver.implicitly_wait(30)
#driver.maximize_window()

# Navigate to the application home page
driver.get("https://www.eurosport.co.uk")

print('Hello World')
