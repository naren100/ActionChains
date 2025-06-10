import subprocess
import time
import signal
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Added this code to start a Python Server, as the data from the local
# Storage was not being managed properly.
server_process = subprocess.Popen(
    ["python3", "-m", "http.server", "8000"],
    cwd="/Users/narendraiyer/PycharmProjects/Python_Dreams/Practice HTML",
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
time.sleep(1)  # Allow the server to start

try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    # Using local server
    driver.get("http://localhost:8000/index.html")

    # Added this code as the local storage was getting corrupted
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()
    time.sleep(1)

    # Create new Employee
    wait.until(EC.element_to_be_clickable((By.ID, "newEmployeeBtn"))).click()
    time.sleep(0.5)
    driver.find_element(By.ID, "empId").send_keys("110")
    driver.find_element(By.ID, "empName").send_keys("Diana Rayzberg")
    driver.find_element(By.ID, "empStatus").send_keys("Regular")
    driver.find_element(By.ID, "empProject").send_keys("Manager of QA GA and Scrum Teams")
    driver.find_element(By.XPATH, "//input[@name='empLocation' and @value='Pittsburgh']").click()

    # Using Flatpickr to input dates
    driver.execute_script("document.getElementById('startDate').removeAttribute('readonly')")
    driver.execute_script("document.getElementById('endDate').removeAttribute('readonly')")
    driver.find_element(By.ID, "startDate").send_keys("2025-06-09")
    driver.find_element(By.ID, "endDate").send_keys("2030-12-31")

    # Save the Form
    driver.find_element(By.XPATH, "//form[@id='empForm']//button[@type='submit']").click()
    time.sleep(3)  # wait for iframe to reload and update

    # Switch to iframe and Find Diana
    iframe = driver.find_element(By.ID, "employeeFrame")
    driver.switch_to.frame(iframe)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Employee List']")))

    # Try and Exept incase Diana's data was not saved
    try:
        row = wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='110']/..")))
        row.click()
    except Exception as e:
        driver.save_screenshot("debug_iframe_missing_diana.png")
        print("ERROR: Diana not found. HTML below:")
        print(driver.page_source)
        raise e

    # SWitching from Iframe to the main page again
    driver.switch_to.default_content()
    time.sleep(0.5)

    #Make Changes to validate the change
    project_input = driver.find_element(By.ID, "empProject")
    project_input.clear()
    project_input.send_keys("Vice President of World Wide QA")

    # Submit Again
    driver.find_element(By.XPATH, "//form[@id='empForm']//button[@type='submit']").click()
    time.sleep(2)

finally:
    driver.quit()
    os.kill(server_process.pid, signal.SIGTERM)
    print("Server has shutdown and driver has been closed.")
