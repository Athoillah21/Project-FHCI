from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

url = "https://rekrutmenbersama.fhcibumn.id/job"

driver = webdriver.Chrome(executable_path='/home/athoillah/Downloads/chromedriver_linux64/chromedriver')
driver.get(url)

driver.implicitly_wait(30)

Jur = [] 

jurusan_path = '/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div/div[1]/div[2]/div/div[5]/select'
j1 = driver.find_element(By.XPATH,jurusan_path).get_attribute('innerText')
Jur.append(j1)

data = pd.DataFrame({
    'Posisi': Posisi,
    'Perusahaan': Perusahaan,
    'Bidang': Bidang,
    'Jenjang': Jenjang,
    'Jurusan': Jurusan,
    'Requirement': Requirement,
    'Link': Links
})

data.to_csv("FHCI_Desember2022.csv", index=False)