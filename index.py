import requests
from selenium import *
from bs4 import BeautifulSoup
from dados import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep


driver = webdriver.Chrome(executable_path='/Users/rafaellaramartins/Desktop/Freelances/boletos/chromedriver')
driver.get(url)


def Login():

    btn_user = driver.find_element(By.ID, 'inputEmail')
    btn_user.send_keys(my_user)
    
    btn_pass = driver.find_element(By.ID, 'inputPassword')
    btn_pass.send_keys(my_pasword)
    
    sleep(3)
    
    btn_Entrar = driver.find_element(By.ID, 'login')
    btn_Entrar.click()
    
    sleep(3)
    
def Faturas():
    
    btn_faturas = driver.find_element(By.XPATH, '//*[@id="main-body"]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/h3/div')
    btn_faturas.click()
    
    sleep(2)
    
    #pendestes = driver.find_elements(By.CLASS_NAME, 'label status status-unpaid')   
    
    
    

response = requests.get(url)

