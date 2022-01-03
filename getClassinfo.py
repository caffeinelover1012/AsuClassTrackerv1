from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-logging")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)

url = r"https://webapp4.asu.edu/catalog/course?r=14731"


token = "2107768431:AAEjv9BXlO8R6m0i5mlp4nM2sb9rvs5brRk"
url_for_api = f"https://api.telegram.org/bot{token}"
def send(text):
    params = {"chat_id": "2107779169", "text":text}
    r = requests.get(url_for_api + "/sendMessage", params=params)


driver.get(url)
sleep(2)
found = driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[1]/span")
print(found[0].text)
print("----------------------------------------------")
