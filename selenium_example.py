from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())


URL = 'https://www.google.com/imghp'

driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)