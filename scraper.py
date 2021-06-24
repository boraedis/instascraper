from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd
import numpy as np
import csv
from bs4 import BeautifulSoup
import re
pd.set_option("display.max_rows", None, "display.max_columns", None)

username = '4704199884'
password = '878878Bora!'

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.instagram.com/gt.classof2025')
sleep(1)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()

usernamebox = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))[0]
usernamebox.send_keys(username)
passwordbox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordbox.send_keys(password)
passwordbox.send_keys(Keys.ENTER)

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')))[0].click()


WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a')))[0].click()

file = open("posts.csv","a")


def collect(page_source):
    try:
        soup = BeautifulSoup(page_source,'html.parser')
        match = soup.find('div',{'class':"C4VMK"})
        dt = re.search(r'datetime="(.*?)"',str(match))

        text = match.text
        text = text.replace(";",",")
        try:
            file.write(f"{dt.group(1)};{text}\n")
        except:
            file.write(f"ERROR : {text}\n")
    except:
        print("ERROR")

sleep(5)
collect(driver.page_source)
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,f'/html/body/div[5]/div[1]/div/div/a')))[0].click()


for i in range(750):
    sleep(6)
    collect(driver.page_source)
    # Next Post
    WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.XPATH,f'/html/body/div[5]/div[1]/div/div/a[2]')))[0].click()

file.close()
# searchbar = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div')))[0]
# searchbar.send_keys("gt.classof2025")
# searchbar.send_keys(Keys.ENTER)

