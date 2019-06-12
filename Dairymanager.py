import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

vlccname=("","Emp1","vlcctest1")
addresstype=("","Emp1","Vlcc")
address=("","2","Pune")
city=("","ewq","Pune")
email=("","sr","vlcctest1@gmail.com")
opname=("","sr","vlcctest1")
centerid=("","re","963852")
campoffice=("","emp","camp office-Camp Office")
chillingcenter=("","emp","chilling Centre-Chilling Centre")
plantoffice=("","emp","plant-Plant")

def addresslist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Address List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Address List Page")
        time.sleep(4)
    except:
        print("Failed")
        d.quit()
        
def tocheckmsg(d):
    try:
        time.sleep(2)
        if d.find_element_by_class_name("msgprint").is_displayed():
            already=d.find_element_by_class_name("msgprint").text
            print(already)  
            d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
            
        elif d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").is_displayed():
            print("required fields ")
            time.sleep(5);                            
            countries=Select(d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[2]/div[1]/ul/li")).options
            for index, value in enumerate(countries):
                print("Mandatory fields required in Lead: "+value.text)
            time.sleep(5);
            d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
    except:
        print("Failed")
        d.quit()        
        
        
        
        
def newvlcc(d):
    try:
        size=vlccname.__len__()
        time.sleep(2)
        addresslist(d)
        time.sleep(10)
        
     
        if d.find_element_by_xpath("//*[@id='page-List/Address']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #print(" found")
            time.sleep(2)
            d.find_element_by_xpath("//*[@id='page-List/Address']/div[1]/div/div/div[2]/button[2]").click()
            time.sleep(2)             
           # for i in range(size): 
            d.find_element_by_xpath("//*[@data-fieldname='address_title'] //input[@type='text']").send_keys(vlccname.__getitem__(2))
            d.find_element_by_xpath("//*[@id='page-Form/Address']/div[1]/div/div/div[2]/button[2]").send_keys(Keys.DOWN)
            d.find_element_by_xpath("").send_keys(Keys.DOWN)
        
            #print("Saving  Contact ")
            #===================================================================
            # d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
            # time.sleep(6);
            # cname1=d.find_element_by_xpath(".//*[@id='page-Form/Customer']/div[1]/div/div/div[1]/h1/div[2]").text
            # #print("Contact name ---"+fname1)
            # time.sleep(3);
            # temp=custname.__getitem__(2)
            # #print("temp name "+temp)
            # time.sleep(3);
            # if cname1==temp:
            #     print("Customer Name :"+cname1+" Customer is created")
            # else:
            #     #print("else condition")
            #     tocheckmsg(d)
            #===================================================================
            
        
    except:
        print("newvlcc Failed")
        d.quit()        