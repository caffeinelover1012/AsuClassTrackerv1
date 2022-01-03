from time import sleep
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
    

def get_data(ccode):
    url = rf"https://webapp4.asu.edu/catalog/course?r={ccode}"
    driver.get(url)
    sleep(2)
    try:
        noresults = driver.find_element(By.CLASS_NAME,"noResults")
    except:
        noresults=None

    if noresults:
        return -1
    else:
        found = driver.find_elements(By.XPATH,"/html/body/div[1]/div[4]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[1]/span")
        res_text = (found[0].text)
        if "Seats Open" not in res_text:
            return 0
        else:
            to_be_ret = res_text.splitlines()
            return [to_be_ret[0],to_be_ret[3].strip()]

seats_not_open = True
init_data = get_data(class_code)
if init_data==-1:
    print("There are no results for this class code.")
elif init_data==0:
    print("Class not open.")
else:
    while seats_not_open:
        data = get_data(class_code)
        print(data[1])
        print(data[0])
