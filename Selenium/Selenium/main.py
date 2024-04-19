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

# What you enter here will be searched for in
# Google Images
query = input('Digite o que deseja buscar')
 
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

############## BAIXAR 1 IMAGEM ##############################
try:
    img = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[13]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/h3/a/div/div/div/g-img/img")
    encontrou_imagem = True
except:
    pass


if encontrou_imagem == False:
    try:
        img = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
        encontrou_imagem = True
    except:
        pass

if encontrou_imagem == False:
    img = driver.find_element(By.XPATH, "//img[@class='YQ4gaf']")
    encontrou_imagem = True

print('erro')

src = img.get_attribute('src')

###############################################################

############### BAIXAR VARIAS IMAGENS #########################
#imagens = driver.find_elements(By.XPATH, "//img[@class='YQ4gaf']")

#for imagem in imagens:
#    print(imagem.get_attribute('src'))


#################################################################

with urlopen(src) as in_stream, open('img.png', 'wb') as out_file:
    copyfileobj(in_stream, out_file)

driver.close()