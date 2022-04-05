from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless") #Use this and the following option to run Headless
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=option)

def main_logic():
    browser.get("https://forms.gle/3zyGrMEqwyh2zVV4A")
    radiobuttons = browser.find_elements(by=By.CLASS_NAME, value="SG0AAe")
    
    for i in radiobuttons:
        all_children_by_xpath = i.find_elements(by=By.XPATH, value=".//*")
        buttons=[]
        for j in all_children_by_xpath:
            if "nWQGrd zwllIb" in j.get_attribute("class"):
                buttons.append(j)
        index=random.randint(0, len(buttons)-1)
        buttons[index].click()

        submitbutton=browser.find_elements(by=By.XPATH,value="/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span")
        submitbutton[0].click()
        sleep(1)        

number_of_responses=4
for i in range(number_of_responses):
    main_logic()
    print("ITERATION:",i+1)