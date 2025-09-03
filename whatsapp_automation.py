import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("WhatsAppAutomation").sheet1

# Read all records
records = sheet.get_all_records()

# Setup Selenium WebDriver (Make sure chromedriver is configured on your system)
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print("Scan QR Code, then press Enter")
input()

for i, record in enumerate(records):
    phone = record['Phone']
    message = record['Message']
    url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"
    driver.get(url)
    time.sleep(10)
    
    # Click send button after message is loaded
    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_btn.click()
    time.sleep(5)
    
    # Update status in sheet
    sheet.update_cell(i+2, 3, 'Sent')

driver.quit()

