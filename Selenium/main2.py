from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from urllib.request import urlopen
from shutil import copyfileobj
import numpy as np

# What you enter here will be searched for in
# Google Images
query = input('Digite o que deseja buscar ')
 
chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("detach", True)

# Creating a webdriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Google Images in the browser
driver.get('https://images.google.com/')

driver.maximize_window()
 
# Finding the search box
box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
 
# Type the search query in the search box
box.send_keys(query)
 
# Pressing enter
box.send_keys(Keys.ENTER)

time.sleep(1)

encontrou_imagem = False

def scroll_to_bottom():
 
    last_height = driver.execute_script('\
    return document.body.scrollHeight')
 
    while True:
        driver.execute_script('\
        window.scrollTo(0,document.body.scrollHeight)')
 
        # waiting for the results to load
        # Increase the sleep time if your internet is slow
        time.sleep(3)
 
        new_height = driver.execute_script('\
        return document.body.scrollHeight')
 
        # click on "Show more results" (if exists)
        try:
            driver.find_element_by_css_selector(".YstHxe input").click()
 
            # waiting for the results to load
            # Increase the sleep time if your internet is slow
            time.sleep(3)
 
        except:
            pass
 
        # checking if we have reached the bottom of the page
        if new_height == last_height:
            break
 
        last_height = new_height
 
scroll_to_bottom()

############### BAIXAR VARIAS IMAGENS #########################
try:
    imagens = driver.find_elements(By.XPATH, "//img[@class='YQ4gaf']")
    # array = []
    teste = 0

    for imagem in imagens:
        print(imagem.get_attribute('src'))
        src = imagem.get_attribute('src')
        # array = np.append(array, imagens)
        teste += 1
        with urlopen(src) as in_stream, open(f'{teste}.png', 'wb') as out_file:
            copyfileobj(in_stream, out_file)
        time.sleep(0.2)
except Exception as e:
    print(e)
    pass
#################################################################

driver.close()