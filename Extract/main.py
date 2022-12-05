from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

url = "https://rekrutmenbersama.fhcibumn.id/job"


driver = webdriver.Chrome(executable_path='/home/athoillah/Downloads/chromedriver_linux64/chromedriver')
driver.get(url)

driver.implicitly_wait(30)

Links = [] 

jobs_block = driver.find_element(By.XPATH, """//*[@id="list"]""")


# Page 1
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 2
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[2]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)


# To Page 3
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[3]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 4
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[4]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 5
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 6
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 7
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 8
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 9
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 10
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 11
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 12
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 13
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 14
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 15
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 16
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 17
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 18
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 19
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 20
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 21
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 22
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 23
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 24
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 25
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 26
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 27
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 28
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 29
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 30
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 31
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)

# To Page 32
driver.find_element(By.XPATH, f"""//*[@id="job_available"]/div/ul[2]/li[5]/a""").click()
time.sleep(3)
link_list = jobs_block.find_elements(By.TAG_NAME,"a")
for link in link_list:
    link0 = link.get_attribute('href')
    Links.append(link0)


print('Found ' + str(len(Links)) + ' for job offers')


Posisi = []
Perusahaan = []
Bidang = []
Jenjang = []
Jurusan = []
Requirement = []

print('Visiting the links and collecting information just started....')

for i in range(len(Links)):
    try:
        driver.get(Links[i])
        i=i+1
        time.sleep(2)
    except:
        pass
    
    try:
        po_path = '/html/body/div[1]/div[3]/div/div/div/div/div[2]/h4/b'
        po0 = driver.find_element(By.XPATH,po_path).get_attribute('innerText')
        Posisi.append(po0)
    except:
        po1 = 'Empty Cause Error Network'
        Posisi.append(po1)
        
    try:
        pe_path = '/html/body/div[1]/div[3]/div/div/div/div/div[2]/p'
        pe0 = driver.find_element(By.XPATH,pe_path).get_attribute('innerText')
        Perusahaan.append(pe0)
    except:
        pe1 = 'Empty Cause Error Network'
        Perusahaan.append(pe1)
        
    try:
        bi_path = '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div/div/div[1]/div[2]/p'
        bi0 = driver.find_element(By.XPATH,bi_path).get_attribute('innerText')
        Bidang.append(bi0)
    except:
        bi1 = 'Empty Cause Error Network'
        Bidang.append(bi1)
        
    try:
        je_path = '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div/div/div[2]/div[2]/p'
        je0 = driver.find_element(By.XPATH,je_path).get_attribute('innerText')
        Jenjang.append(je0)
    except:
        je1 = 'Empty Cause Error Network'
        Jenjang.append(je1)
    #_________________________________________________________________________Jurusan
    try:
        ju_path = '/html/body/div[1]/div[4]/div/div/div[1]/div/div[1]/div/ol'
        ju0 = driver.find_element(By.XPATH,ju_path).get_attribute('innerText')
        Jurusan.append(ju0)
    except:
        try:
            ju_path1 = '/html/body/div[1]/div[4]/div/div/div[1]/div/div[1]/div/p'
            ju1 = driver.find_element(By.XPATH,ju_path1).get_attribute('innerText')
            Jurusan.append(ju1)
        except:
            ju2 = 'Empty Cause Error Network'
            Jurusan.append(ju2)
    
    #_________________________________________________________________________Requirement
    try:
        re_path = '/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div/ol'
        re0 = driver.find_element(By.XPATH,re_path).get_attribute('innerText')
        Requirement.append(re0)
    except:
        try:
            re_path1 = '/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div/ul'
            re1 = driver.find_element(By.XPATH,re_path1).get_attribute('innerText')
            Requirement.append(re1)
        except:
            try:
                re_path2 = '/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div'
                re2 = driver.find_element(By.XPATH,re_path2).get_attribute('innerText')
                Requirement.append(re2)
            except:
                re3 = 'Empty Cause Error Network'
                Requirement.append(re3)
        
    print("Current at: ", i, ", Percentage at: ", (i+1)/len(Links)*100, "%",end="\r")


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






































# //*[@id="job_available"]/div/ul[2]/li[2]/a # 1 --> 2
# //*[@id="job_available"]/div/ul[2]/li[3]/a # 2 --> 3
# //*[@id="job_available"]/div/ul[2]/li[4]/a # 3 --> 4
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 4 --> 5
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 5 --> 6
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 6 --> 7
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 7 --> 8
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 8 --> 9
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 9 --> 10
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 10 --> 11
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 11 --> 12
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 12 --> 13
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 13 --> 14
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 14 --> 15
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 15 --> 16
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 16 --> 17
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 17 --> 18
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 18 --> 19
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 19 --> 20
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 20 --> 21
# //*[@id="job_available"]/div/ul[2]/li[5]/a # 21 --> 22
