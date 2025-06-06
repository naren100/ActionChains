from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

options = Options()
options.add_argument("--width=1920")
options.add_argument("--height=1080")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.letskodeit.com/practice")
time.sleep(3)

total_width = driver.execute_script("return document.body.scrollWidth")
viewport_width = driver.execute_script("return window.innerWidth")

print(f"Total page width: {total_width}px")
print(f"Viewport width: {viewport_width}px")

if total_width > viewport_width:
    driver.execute_script("window.scrollTo(arguments[0], 0);", total_width)
    print("Scrolled horizontally to the right.")
else:
    print("Page does not require horizontal scrolling.")

time.sleep(5)
driver.quit()
