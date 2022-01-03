from time import sleep
from types import resolve_bases
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-logging")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)

# class_code = '14731'

while True:
    class_code = input("Enter 5 digit class number: ")
    if int(class_code) not in range(9999,100000):
        print("Sorry, invalid class code.")
        continue
    else:
        #we're happy with the value given.
        #we're ready to exit the loop.
        break
    
url = rf"https://webapp4.asu.edu/catalog/course?r={class_code}"

driver.get(url)
sleep(2)

found = driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[1]/span")
try:
    noresults = driver.find_element(By.CLASS_NAME,"noResults")
except:
    noresults=None

if noresults:
    print("NO CLASS FOUND WITH GIVEN CRITERIA.")
else:
    res_text = (found[0].text)
    if "Seats Open" not in res_text:
        print("Class not open!")
    else:
        print(res_text)
    print("----------------------------------------------")
