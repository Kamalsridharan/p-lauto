from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import glob

# Use virtual display for headless execution
# (This is not needed if running on a system with a display)
# with Display():
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

# Use webdriver_manager to automatically download and manage the ChromeDriver executable
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def download_csv(url, destination_folder, file_name):
    try:
        driver.set_window_size(1200, 800)
        driver.get(url)

        # Wait for the Export button to be clickable
        export_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Export')]"))
        )

        # Click the Export button
        export_button.click()

        # Wait for the download to complete (adjust the sleep time as needed)
        time.sleep(5)

        # Identify the latest downloaded file
        list_of_files = glob.glob(os.path.join(destination_folder, '*'))
        latest_file = max(list_of_files, key=os.path.getctime)

        # Move the file to the desired location with the specified name
        new_file_path = os.path.join(destination_folder, file_name)
        os.rename(latest_file, new_file_path)

    finally:
        # Close the browser window
        driver.quit()

# URLs and corresponding file names
url_and_file_names = [
    ("https://app.revenuecat.com/charts/revenue?chart_type=Stacked%20area&conversion_timeframe=7%20days&customer_lifetime=30%20days&filter=store%3A%3D%3Aplay_store&range=Last%207%20days%3A2023-11-17%3A2023-11-23&segment=country", "path_in_github_repository", "play.csv"),
    ("https://app.revenuecat.com/charts/revenue?chart_type=Stacked%20area&conversion_timeframe=7%20days&customer_lifetime=30%20days&filter=store%3A%3D%3Aapp_store&range=Last%207%20days%3A2023-11-17%3A2023-11-23&segment=country", "path_in_github_repository", "ios.csv")
]

for url, destination, file_name in url_and_file_names:
    download_csv(url, destination, file_name)
