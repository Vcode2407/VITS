# WhatsApp + Google Sheets Automation

## Project Overview
This project automates sending WhatsApp messages using phone numbers and message texts stored in a Google Sheet. 
The Python script reads the data from Google Sheets, sends WhatsApp messages via WhatsApp Web using Selenium automation, 
and updates the Google Sheet with the status of each message ("Sent") for tracking purposes.

## Features
- Connects to Google Sheets API to fetch phone numbers and messages.
- Automates WhatsApp Web to send messages automatically.
- Updates the Google Sheet with message status after sending.
- Easy to set up and customize.

## Prerequisites
- Python 3 installed on your system.
- Google Cloud Platform project with Google Sheets API enabled.
- Service Account credentials JSON file (`credentials.json`) downloaded.
- Google Sheet prepared with columns: Phone, Message, Status.
- Chrome browser and ChromeDriver installed (compatible versions).

## Google Sheet Setup
Your Google Sheet should have the following columns in the first sheet:

| Phone       | Message                   | Status |
|-------------|---------------------------|--------|
| 15551234567 | Hello from automation!    | Sent   |

- Share this Google Sheet with your Google Service Account email to grant read/write access.

## Installation and Setup

1. Put your `credentials.json` file in the project folder.

2. Install the required Python dependencies using the following command:

   pip install gspread oauth2client selenium

   

3. Download and install ChromeDriver compatible with your Chrome browser version and add it to your system PATH.

## Usage

1. Run the automation script:

python whatsapp_automation.py


2. The script will open WhatsApp Web in a Chrome browser window.

3. Scan the QR code using your WhatsApp mobile app to log in.

4. The script will send messages from the sheet and update the "Status" column with "Sent" after each message.

## Security
- Keep your `credentials.json` file safe and never share it publicly.
- This script uses WhatsApp Web, so your WhatsApp account must be active and connected during the automation.

## Troubleshooting
- If messages are not sending, verify your internet connection and ensure WhatsApp Web is logged in.
- Verify the phone numbers are in the correct international format without spaces or special characters.
- Check that ChromeDriver version matches your Chrome browser version.

## License
This project is open-source and free to use.

---

Feel free to customize this project according to your needs and scale it as per use case.

