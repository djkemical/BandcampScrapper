'''
Created on 20 jun. 2019

@author: Kemical
'''

import configparser
import time
from WebDriver import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class WebDriver:

    def __init__(self, urlSite):
        self.urlSite = urlSite

    def load_settings(self):
        
        """
        Loading and assigning global variables from our settings.txt file
        """
        
        config_parser = configparser.RawConfigParser()
        config_file_path = 'mysettings.txt'
        config_parser.read(config_file_path)

        browser = config_parser.get('your-config', 'BROWSER')
        browser_path = '/Users/Kemical/Downloads/chromedriver'
        name = config_parser.get('your-config', 'NAME')
        page = config_parser.get('your-config', 'PAGE')

        settings = {
            'browser': browser,
            'browser_path': '/Users/Kemical/Downloads/chromedriver',
            'name': name,
            'page': self.urlSite
        }
        return settings

    def load_driver(self, settings):
        
        """
        Load the Selenium driver depending on the browser
        (Edge and Safari are not running yet)
        """
        
        driver = ''

        if settings['browser'] == 'firefox':
            firefox_profile = webdriver.FirefoxProfile(settings['browser_path'])
            driver = webdriver.Firefox(firefox_profile)
        elif settings['browser'] == 'edge':
            pass
        elif settings['browser'] == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(
                "user-data-dir=" + settings['browser_path'])
            driver = webdriver.Chrome('/Users/Kemical/Downloads/chromedriver')
        elif settings['browser'] == 'safari':
            pass

        return driver

    def search_chatter(self, driver, settings):
        
        """
        Function that search the specified user and activates his chat
        """

        wait = WebDriverWait(driver, 600)
        x_arg = '//span[contains(@title,' + settings['name'] + ')]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()

    def read_last_in_message(self, driver):
        
        """
        Reading the last message that you got in from the chatter
        """
        
        message = ''

        for messages in driver.find_elements_by_css_selector('span.selectable-text'):
            if 'bandcamp.com' in messages.text:
                message = messages.text
        return message