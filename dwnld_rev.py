from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--window-size=1920,1080')

# Set the download directory
download_directory = r'C:\Users\KamalDhass\OneDrive\Documents\Feels\RevCat\iOS'
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
})

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the login URL
login_url = "https://app.revenuecat.com/login"
driver.get(login_url)

# Log in
try:
    # Type the username
    username_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/form/div[2]/div[2]/div/input")
    username_input.send_keys("developers@feels-app.com")

    # Click the Log in button
    login_button1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/form/div[4]/button")
    login_button1.click()

    # Wait for the login to complete
    WebDriverWait(driver, 20).until(EC.url_contains("revenuecat.com"))

    # Type the password
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/form/div[3]/div/div[2]/div/input"))
    )
    password_input.send_keys("Tz@5YNc2.RT9eyZ")

    # Click the Log in button again
    login_button2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/form/div[4]/button")
    login_button2.click()

    # Wait for the login to complete
    WebDriverWait(driver, 20).until(EC.url_contains("revenuecat.com"))

    # Navigate to the download URL
    download_url = "https://app.revenuecat.com/charts/revenue?chart_type=Stacked%20area&conversion_timeframe=7%20days&customer_lifetime=30%20days&filter=store%3A%3D%3Aplay_store&range=Last%207%20days%3A2023-11-17%3A2023-11-23&segment=country"
    driver.get(download_url)

    # Wait for the page to load
    time.sleep(5)

    # Find and click the download button using an explicit wait
    download_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/a/button"))
    )
    download_button.click()

    # Wait for the file to be downloaded
    time.sleep(15)  # Adjust the time based on the file size and network speed

finally:
    # Ensure you quit the driver even if an exception occurs
    driver.quit()
