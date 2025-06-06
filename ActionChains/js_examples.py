import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open W3Schools
    driver.get("https://www.w3schools.com/")
    time.sleep(2)
    print("[1] Opened W3Schools homepage")

    # Step 2: Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    print("[2] Scrolled to bottom")

    # Step 3: Scroll back to top
    driver.execute_script("window.scrollTo(250, 500);")
    time.sleep(2)
    print("[3] Scrolled back to top")

    # Step 4: Highlight the "Learn HTML" button
    learn_html_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@class, 'w3-button') and contains(text(), 'Learn HTML')]"))
    )
    driver.execute_script("arguments[0].style.border='3px solid red';", learn_html_button)
    print("[4] Highlighted the 'Learn HTML' button")
    time.sleep(2)

    # Step 5: Try JS click and wait for heading; fallback if network or nav fails
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", learn_html_button)
        driver.execute_script("arguments[0].click();", learn_html_button)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'HTML Tutorial')]")))
        print("[5] Clicked 'Learn HTML' and confirmed HTML Tutorial page loaded")
    except Exception as e:
        print("[5] Navigation failed. Reason:", e)
        print("[5] Using fallback: Navigating directly to HTML Tutorial page...")
        driver.get("https://www.w3schools.com/html/default.asp")
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'HTML Tutorial')]")))
        print("[5] Fallback successful: HTML Tutorial page loaded directly")

    time.sleep(2)

    # Step 6: Modify the heading text
    heading = driver.find_element(By.XPATH, "//h1[contains(text(),'HTML Tutorial')]")
    driver.execute_script("arguments[0].textContent = 'Modified by Selenium';", heading)
    print("[6] Modified page heading text")
    time.sleep(2)

    # Step 7: Inject a floating message
    driver.execute_script("""
        let newDiv = document.createElement('div');
        newDiv.textContent = 'Hello from Selenium';
        newDiv.style.cssText = 'position:fixed;top:10px;left:10px;background:yellow;padding:10px;z-index:9999;';
        document.body.appendChild(newDiv);
    """)
    print("[7] Injected new floating message into the page")
    time.sleep(3)

    # Step 8: Read page title via JavaScript
    title = driver.execute_script("return document.title;")
    print(f"[8] Page title via JavaScript: '{title}'")

finally:
    driver.quit()
    print("[9] Test complete. Browser closed.")


