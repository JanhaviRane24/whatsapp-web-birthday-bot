from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

# Your ChromeDriver path
driver_path = "C:/Users/ranej/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for manual QR code scan
print("Please scan the QR code on your phone...")
time.sleep(30)  # You can increase if needed

# Target contact and message
contact_name = "Pappa"
message = "Happy birthday pappa"

try:
    # Wait for overlay dialog and close it if it appears
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]'))
    )
    close_button = driver.find_element(By.XPATH, '//div[@role="dialog"]//button')
    close_button.click()
    print("Closed modal dialog.")
except TimeoutException:
    # No modal appeared – continue normally
    print("No modal to close.")

# Now continue to click the search box
search_box = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
)
search_box.click()

try:
    # Wait for search box and enter contact name
    search_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    search_box.click()
    search_box.send_keys(contact_name)
    time.sleep(2)

    # Click the chat
    contact = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]'))
    )
    contact.click()
    time.sleep(1)

    # Type and send message
    msg_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )
    msg_box.send_keys(message)
    msg_box.send_keys('\n')  # Press Enter to send

    print(f"Message sent to {contact_name}!")

except Exception as e:
    print("Something went wrong:", e)

finally:
    time.sleep(5)
    driver.quit()
