from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Setup
options = Options()
options.add_argument("--start-maximized")  # Ensure the window is maximized
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://github.com/")

    # Wait for the 'Sign in' link to be present
    sign_in_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))

    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_element)

    # Use JavaScript to click the element
    driver.execute_script("arguments[0].click();", sign_in_element)

    # Optional: Verify navigation
    wait.until(EC.url_contains("/login"))
    print("Successfully navigated to the login page.")

finally:
    driver.quit()







