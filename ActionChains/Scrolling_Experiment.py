from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Setup Firefox driver using WebDriver Manager
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Open the Let's Kode It website
driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()

# Wait for the page to load
time.sleep(6)

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled to bottom")
time.sleep(6)

# Scroll back to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
print("Scrolled to top")
time.sleep(6)

# Close the browser
driver.quit()
