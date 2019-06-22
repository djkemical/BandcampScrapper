'''
Created on 20 jun. 2019

@author: Kemical
'''

"""
Importing the libraries that we are going to use
for loading the settings file and scraping the website
"""

import configparser
import time
from WebDriver import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def main():

    # Whatsapp Driver
    wapp = WebDriver('https://web.whatsapp.com')
    wappSettings = wapp.load_settings()
    wappDriver = wapp.load_driver(wappSettings)
    wappDriver.get(wappSettings['page'])
    wapp.search_chatter(wappDriver, wappSettings)

    previous_in_message = ''
    while True:
        last_in_message = wapp.read_last_in_message(wappDriver)

        if previous_in_message != last_in_message:
            print(last_in_message)
            previous_in_message = last_in_message

        time.sleep(1)


if __name__ == '__main__':
    main()