import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

try:
    # Step 1: Open Selenium Playground
    driver.get("https://www.lambdatest.com/selenium-playground/")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
    print("[1] Opened Selenium Playground")
    time.sleep(2)

    # Step 2: Click + Send Keys in Simple Form
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
    wait.until(EC.presence_of_element_located((By.ID, "user-message")))
    input_field = driver.find_element(By.ID, "user-message")
    show_button = driver.find_element(By.ID, "showInput")
    actions.click(input_field).pause(1).send_keys("Hello ActionChains").pause(1).click(show_button).perform()
    print("[2] Performed click and send_keys")
    time.sleep(2)

    # Step 3: Ctrl + A
    actions.click(input_field).pause(1).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    print("[3] Performed key down + key up: Ctrl+A")
    time.sleep(2)

    # Step 4: Slider Drag
    driver.get("https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo")
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='range']")))
    slider = driver.find_element(By.XPATH, "//input[@type='range']")
    actions.click_and_hold(slider).pause(1).move_by_offset(50, 0).pause(1).release().perform()
    print("[4] Performed click and hold + drag slider")
    time.sleep(2)

    # Step 5: Context Menu
    driver.get("https://www.lambdatest.com/selenium-playground/context-menu")
    wait.until(EC.presence_of_element_located((By.ID, "hot-spot")))
    box = driver.find_element(By.ID, "hot-spot")
    actions.context_click(box).perform()
    print("[5] Performed right-click (context click)")
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(2)

    # Step 6: Double-click inside jQuery iframe
    driver.get("https://api.jquery.com/dblclick/")
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
    box = wait.until(EC.presence_of_element_located((By.TAG_NAME, "div")))
    actions.double_click(box).perform()
    print("[6] Performed double-click inside jQuery iframe")
    driver.switch_to.default_content()
    time.sleep(2)

    # Step 7: Drag and Drop
    driver.get("https://www.lambdatest.com/selenium-playground/drag-and-drop-demo")
    wait.until(EC.presence_of_element_located((By.ID, "draggable")))
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions.drag_and_drop(source, target).pause(1).perform()
    print("[7] Performed drag and drop")
    time.sleep(2)

    # Step 8: Hover
    driver.get("https://www.lambdatest.com/selenium-playground/")
    hover_link = driver.find_element(By.LINK_TEXT, "Checkbox Demo")
    actions.move_to_element(hover_link).pause(1).perform()
    print("[8] Hovered over 'Checkbox Demo' link")
    time.sleep(2)

finally:
    driver.quit()
    print("[9] Browser closed. Test complete.")


