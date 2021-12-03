#!/bin/python

"""
Scrap an onion adress based on HTML classes
"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd
import sys

# TODO open tor browser with selenium
binary = FirefoxBinary("~/Apps/tor-browser_en-US/Browser/firefox")
driver = webdriver.Firefox(firefox_binary = binary)

if len(sys.argv) == 1:
    print("Specify hidden service url as a first argument")
    print("and class name as a second.")
    print("Example : python {sys.argv[0]} [url] [class name]")

url = sys.argv[1]
class_name = sys.argv[2]
driver.get(url)
elements = driver.find_elements_by_class_name(class_name)

for element in elements:
    print(element)

# export to CSV

df['elements'] = elements
df.to_csv('scraped.csv')
