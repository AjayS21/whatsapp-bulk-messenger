from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import time

# Automatically download and update ChromeDriver to the latest version
print("Initializing WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Get the ChromeDriver version
chrome_driver_version = driver.capabilities['chrome']['chromedriverVersion']
print(f'Installed ChromeDriver version: {chrome_driver_version}')

# Config
login_time = 60     # Time for login (in seconds)
new_msg_time = 20   # Time for a new message (in seconds)
send_msg_time = 20  # Time for sending a message (in seconds)
country_code = 91   # Set your country code

# Encode Message Text
print("Reading message text from file...")
with open('message.txt', 'r') as file:
    msg = quote(file.read())

# Open browser with default link
print("Opening WhatsApp Web...")
link = 'https://web.whatsapp.com'
driver.get(link)
print("Waiting for login...")
time.sleep(login_time)

# Function to send an image with optional text
def send_image_with_text(driver, num, image_path, text=None):
    try:
        print(f"Navigating to chat with {num}...")
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)

        print("Clicking on the attachment icon...")
        attachment_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]'))
        )
        attachment_icon.click()

        print("Selecting 'Photos & Videos' from the attachment options...")
        photos_videos_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
        )
        photos_videos_option.send_keys(image_path)
        
        # Optionally, add text to the message
        if text:
            print("Adding text to the message...")
            message_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x1lkfr7t' and @contenteditable='true']"))
            )
            message_input.send_keys(text)
            time.sleep(new_msg_time)  # Wait to ensure text is fully added

        print("Clicking the send button...")
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
        )
        send_button.click()
        print(f"Message sent to {num}")
    except Exception as e:
        print(f"An error occurred while sending message to {num}: {str(e)}")

# Loop through numbers list
print("Reading numbers from file...")
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.strip()
        image_path = 'C:\\New folder\\Projects\\Whatsapp Message Sender in bulk - Copy\\Whatsapp.jpeg'  # Replace with the actual image file path
        # Read the message from 'message.txt'
        with open('message.txt', 'r') as message_file:
            text_to_send = message_file.read()
        send_image_with_text(driver, num, image_path, text_to_send)
        time.sleep(send_msg_time)

print("Quitting the driver...")
driver.quit()
