import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

# Define the path to the extension folder
#extension_folder = '/home/user/adblock'

options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Load the extension by specifying the extension folder
#options.add_argument(f'--load-extension={extension_folder}')

while True:
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get("https://yourlink.com/")
        print(driver.title)

        time.sleep(2)

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if driver:
            driver.quit()  # Use quit() to properly close the browser and free resources

    time.sleep(60)  # Wait for 60 seconds before starting the next iteration
