from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup driver
options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# Go to GitHub
driver.get("https://github.com/")

# Try robust way to click Sign in
sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']")))
sign_in.click()

# Optional: check URL
print("Navigated to:", driver.current_url)

driver.quit()
