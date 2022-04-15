from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import smtplib
import sys

from email.message import EmailMessage
from time import sleep

# Target URL:
url = ("https://www.bestbuy.ca/en-ca/product/nvidia-geforce-"
       "rtx-3070-8gb-gddr6-video-card-only-at-best-buy/15078017")
# Test URL:
test_url = ("https://www.bestbuy.ca/en-ca/product/msi-geforce-gtx-1660-"
            "ti-gaming-x-6g-geforce-gtx-1660-ti-graphic-card-6-gb-gddr6/13456384")

# Enables chrome to run in background.
chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Clicks "Add to cart" button and determines if it's active:
element = driver.find_element_by_xpath('''//*[@id="test"]/button''')
element.click()
print(element.is_enabled())

if element.is_enabled():
    # Email recipients:
    recipients = ['tristinmanson@gmail.com', 'damonrobertgeelen@gmail.com']

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('tristinmanson@gmail.com', 'Zz132ABab04')

    for recipient in recipients:

        with open('text_files/notification.txt') as fo:
            msg = EmailMessage()
            msg.set_content(fo.read())

        msg['Subject'] = 'RTX-3070 Restocked!'
        msg['From'] = 'tristinmanson@gmail.com'
        msg['To'] = f'{recipient}'
        s.send_message(msg)

    s.quit()

else:
    # Don't email:
    print('RTX-3070 is not in stock: not emailing...')

driver.close()
# This sleep call just keeps the cmd.exe window from closing immediately when this program ends.
sleep(5)
sys.exit()







