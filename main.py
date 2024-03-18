from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.fahasa.com/sach-trong-nuoc/van-hoc-trong-nuoc.html?order=num_orders&limit=48&p=1")

input_element = driver.find_elements(By.XPATH,'//*[@id="products_grid"]/li')
#input_element_price = driver.find_elements(By.XPATH,'//*[@id="products_grid"]/li')

name = []
price = []
old_price = []
image = []

for i in input_element:
    try :
        name.append(i.find_element(By.XPATH,'./div/div[2]/h2/a').text)
    except :
        name.append("Hàng Sắp về")

for i in input_element:
    try:
        price.append(i.find_element(By.XPATH,'./div/div/div/span/span/p').text)
    except:
        price.append("Hàng Sắp Về")
    
        

for i in input_element:
    try:
        old_price.append(i.find_element(By.XPATH,'./div/div/div/span/span/p[2]').text)
    except:
        old_price.append("hàng sắp về")
    #price.append(i.find_element(By.XPATH,'./div/div/div/span/span/p[2]').text)

for i in input_element:
    # print(i.find_element(By.XPATH,'./div/div/div/div/a/span/img').get_attribute('data-src'))
    image.append(i.find_element(By.XPATH,'./div/div/div/div/a/span/img').get_attribute('data-src'))


df = pd.DataFrame({"name":name,"image":image,"price":price,"old_price":old_price})
df.to_csv("product.csv",index=False)
time.sleep(5)
