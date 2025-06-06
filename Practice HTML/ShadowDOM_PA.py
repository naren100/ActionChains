from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("file:///Users/narendraiyer/PycharmProjects/Python_Dreams/Practice%20HTML/Shadow_DOMS.html")

wait = WebDriverWait(driver, 10)
host = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "hello-button")))
shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
button = shadow_root.find_element(By.CSS_SELECTOR, "#sayHelloBtn")
button.click()

# Verify alert appeared after click
try:
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    print("Button clicked: Alert text =", alert.text)
    alert.accept()
except:
    print("Button click failed: All Tek's fault.")

driver.quit()

