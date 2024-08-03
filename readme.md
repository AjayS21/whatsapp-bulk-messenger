# WhatsApp Bulk Message Sender

This script allows you to send bulk WhatsApp messages with optional images using Selenium WebDriver. You can specify a list of phone numbers and a message to be sent, along with an optional image attachment.

## Features

- Send text messages to multiple WhatsApp contacts
- Attach images to messages
- Automatically open WhatsApp Web and navigate through the interface

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (automatically installed by the script)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/whatsapp-bulk-message-sender.git
   cd whatsapp-bulk-message-sender

2. **Install the required Python packages::**

pip install -r requirements.txt

3. **Ensure you have the correct version of ChromeDriver installed. You can download it from ChromeDriver.**

Usage
1. Prepare your data files:

numbers.txt: List of phone numbers (one per line).
message.txt: Text message to send.
image.jpg: Path to the image you want to send.

2. Run the script: python main.py

Code Explanation
main.py: Contains the logic to send messages and images using Selenium WebDriver.
Initializes WebDriver and navigates to WhatsApp Web.
Reads phone numbers and message text from files.
Sends messages and images to each phone number.
Troubleshooting
Error: File not found: Ensure the file path for the image is correct.
Error: Element not found: Update the XPath selectors if WhatsApp Web's structure changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.