import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

itemname=("","Emp1","Laptop")
itemcode=("", "asds","104")
qty=("","m","2")
itemgroup=("","asd","Products")
unit=("", "feb12","Nos")
openingstock=("","Emp1","500")
rate=("","m","25000")


def itemlist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Item List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Item List Page")
        time.sleep(2)
    except:
        print("Failed")
        d.quit()
        
def newitem(d):
    try:
        size=itemname.__len__()
        time.sleep(2)
        itemlist(d)
        time.sleep(3)                
        if d.find_element_by_xpath("//*[@id='page-List/Item']/div[1]/div/div/div[2]/button[2]/span").is_displayed():
            #print(" found")
            time.sleep(2)
            d.find_element_by_xpath("//*[@id='page-List/Item']/div[1]/div/div/div[2]/button[2]/span").click()
            time.sleep(2)
            d.find_element_by_xpath("//button[text()='Edit in full page for more options like assets, serial nos, batches etc.']").click()
            #form filling
            for i in range(size): 
                
                item_code="//*[@data-fieldname='item_code'] //input[@type='text']"
                time.sleep(2)
                d.find_element_by_xpath(item_code).clear()
                time.sleep(2)
                d.find_element_by_xpath(item_code).send_keys(itemcode.__getitem__(i))
                
                item_name="//*[@data-fieldname='item_name'] //input[@type='text']"
                time.sleep(2)
                d.find_element_by_xpath(item_name).clear()
                time.sleep(2)
                d.find_element_by_xpath(item_name).clear()
                time.sleep(2)
                d.find_element_by_xpath(item_name).send_keys(itemname.__getitem__(i))
                
                item_group="//*[@data-fieldname='item_group'] //*[@data-doctype='Item']"
                time.sleep(1)
                #d.find_element_by_xpath(item_group).clear()
                time.sleep(1)
                d.find_element_by_xpath(item_group).send_keys(itemgroup.__getitem__(i))     
                       
                stock_uom="//*[@data-fieldname='stock_uom'] //*[@data-doctype='Item']"           
                time.sleep(1)
                #d.find_element_by_xpath(stock_uom).clear()
                time.sleep(1)
                d.find_element_by_xpath(stock_uom).send_keys(unit.__getitem__(i))
                
                opening_stock="//*[@data-fieldname='opening_stock'] //input[@type='text']"           
                time.sleep(1)
                d.find_element_by_xpath(opening_stock).clear()
                time.sleep(1)
                d.find_element_by_xpath(opening_stock).send_keys(openingstock.__getitem__(i))
                
                standard_rate="//*[@data-fieldname='standard_rate'] //input[@type='text']"          
                time.sleep(1)
                d.find_element_by_xpath(standard_rate).clear()
                time.sleep(1)
                d.find_element_by_xpath(standard_rate).send_keys(rate.__getitem__(i))
               
                time.sleep(2)
                d.find_element_by_xpath("//*[@id='page-Form/Item']/div[1]/div/div/div[2]/button[2]/span").click()
                time.sleep(3)                                 
                Itemcreated=d.find_element_by_xpath("//*[@id='page-Form/Item']/div[1]/div/div/div[1]/h1").text
                
                time.sleep(1);
                temp=itemname.__getitem__(2)+" Enabled"
                #print("temp name --"+temp)
                #print(" get text"+Itemcreated)
                time.sleep(1);
                if Itemcreated==temp:
                    print("Item Name :"+itemname.__getitem__(2)+"  is created")
                else:
                    #print("else condition")
                    time.sleep(2)
                    if d.find_element_by_class_name("msgprint").is_displayed():
                        already=d.find_element_by_class_name("msgprint").text
                        print(already)  
                        d.find_element_by_xpath("/html/body/div[23]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
                        time.sleep(3)
                        
                    elif d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").is_displayed():
                        #print("required fields ")
                        time.sleep(5);
                        countries=Select(d.find_element_by_class_name("msgprint")).options
                        for index, value in enumerate(countries):
                            print("Mandatory fields required in Lead: "+value.text)
                        time.sleep(5);
                        d.find_element_by_xpath("/html/body/div[23]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
                        time.sleep(3)
                
            
        
    except:
        print("Failed")
        d.quit()        