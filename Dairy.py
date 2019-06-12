import unittest
from selenium import webdriver
import time
import Dairymanager



urlver10="http://uat.pvtdairy.indictranstech.com"
username="dairymanager@gmail.com"
pwd="admin"
d=webdriver.Chrome(executable_path="/home/indic/Documents/rehan/selenium data/chromedriver")
       
def loginfun():

    try:   
        d.get(urlver10)
        d.maximize_window()
        time.sleep(1)
        d.find_element_by_id("login_email").send_keys(username)
        d.find_element_by_id("login_password").send_keys(pwd)      
        d.find_element_by_xpath(".//*[@id='page-login']/div/div/div[2]/section[1]/div[1]/form/button").click() 
        time.sleep(2)
        url=d.title
        
        if url=="Desktop":
            print("Login Sucessfully")
            time.sleep(1)
            if d.find_element_by_class_name("modal-title").is_displayed():
                time.sleep(2)
                d.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[1]").click()
                time.sleep(5)
                
    except:
        print("Login Failed")
        d.quit()
        
loginfun()
Dairymanager.newvlcc(d)



time.sleep(4)
d.quit()

