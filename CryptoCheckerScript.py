from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def navigate_to_coingecko():
    """
    Opens Google Chrome and navigates to coingecko.com.
    """
    # 1. Specify the path to the ChromeDriver executable
    #    -  Important: Download the correct version of ChromeDriver for your Chrome browser.
    #    -  You can download it from: https://chromedriver.chromium.org/downloads
    #    -  Extract the executable and place it in a known location (e.g., /usr/local/bin on Linux/macOS, or a directory in your PATH on Windows).
    #    -  Update the 'executable_path' below to the actual path.
    chrome_driver_path = '/path/to/chromedriver'  # <--- !!! UPDATE THIS PATH !!!

    # 2. Create a Chrome Service object
    service = Service(executable_path=chrome_driver_path)

    # 3. Start a new Chrome browser instance using the Service object
    driver = webdriver.Chrome(service=service)

    # 4. Navigate to coingecko.com
    driver.get("https://www.coingecko.com")

    # 5. (Optional)  Add a short delay to keep the browser window open for a moment.
    #    -  This allows you to see that the script has successfully navigated to the site.
    time.sleep(5)

    # 6. Close the browser window
    driver.quit()

if __name__ == "__main__":
    navigate_to_coingecko()
