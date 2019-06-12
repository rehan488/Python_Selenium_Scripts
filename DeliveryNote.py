import time
import re
import Item
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



custname=("","Emp1","Testcust1")

leadname=("","sr","LEAD-00007")



def deliverynotelist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Delivery Note List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Delivery Note List Page")
        time.sleep(2)
    except:
        print(" list Failed")
        d.quit()
        
def tocheckmsg(d):
    try:
        time.sleep(2)
        if d.find_element_by_class_name("msgprint").is_displayed():
            already=d.find_element_by_class_name("msgprint").text
            print(already)      
            d.find_element_by_xpath("/html/body/div[16]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
            
        elif d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").is_displayed():
            print("required fields ")
            time.sleep(5);                        
            countries=Select(d.find_element_by_xpath("/html/body/div[16]/div[2]/div/div[2]/div[1]/ul/li")).options
            for index, value in enumerate(countries):
                print("Mandatory fields required in Lead: "+value.text)
            time.sleep(5);
            d.find_element_by_xpath("/html/body/div[16]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
    except:
        print(" msg Failed")
        d.quit()   
        
   
def newdeliverynote(d):
    try:
        size=custname.__len__()
        deliverynotelist(d)
        time.sleep(2)
                                      
        if d.find_element_by_xpath(".//*[@id='page-List/Delivery Note']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Delivery Note']/div[1]/div/div/div[2]/button[2]").click()
            #print(" after new ")
        
            for i in range(size):    
                xquoname="//*[@data-fieldname='customer'] //*[@data-doctype='Delivery Note']"
                #d.find_element_by_xpath(xquoname).clear()
                time.sleep(1)
                d.find_element_by_xpath(xquoname).send_keys(custname.__getitem__(i))
                time.sleep(1)
                
                if i==2:
                    d.find_element_by_xpath(xquoname).send_keys(Keys.ENTER)
                    time.sleep(1)            
                    d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[3]/div/div[1]/button[3]").click()
                    
                    time.sleep(4)             
                    d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[2]").click()
                    time.sleep(4)  
                    d.find_element_by_xpath("//*[@data-fieldname='item_code'] //*[@ data-doctype='Delivery Note Item']").send_keys(Item.itemcode.__getitem__(i))
                    time.sleep(1)
                    
                    time.sleep(2)
                    d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div[1]/div[7]/a/span").click()
                    time.sleep(1)
                    d.find_element_by_xpath("//*[@data-fieldname='warehouse'] //*[@ data-doctype='Delivery Note Item']").clear()
                    time.sleep(1)
                    d.find_element_by_xpath("//*[@data-fieldname='warehouse'] //*[@ data-doctype='Delivery Note Item']").send_keys("Stores - I")
                    time.sleep(2)                
                    
                    time.sleep(2)
                    #d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button[1]/span").click()
                    d.find_element_by_xpath("//*[@data-fieldname='warehouse'] //*[@ data-doctype='Delivery Note Item']").send_keys(Keys.ESCAPE)
                    time.sleep(2)
        
        
                print("Saving  deliverynote ")
               
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                time.sleep(4);                  
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Delivery Note']/div[1]/div/div/div[1]/h1").text
                #print(" ---"+fname1)
                temp=custname.__getitem__(2)
                
                if fname1==temp+" Draft":
                    #print(" - Save Draft ")
                    
                    d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Submit']").click()
                    time.sleep(2)             
                    d.find_element_by_xpath("/html/body/div[23]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
                
                time.sleep(1)
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Delivery Note']/div[1]/div/div/div[1]/h1").text
                #print("temp name "+fname1)
                time.sleep(2)
                if fname1==temp+" To Bill":
                    print("Delivery Note Name :"+temp+" is created")
                else:
                    tocheckmsg(d)
                    
            print
        
    except:
        print("new Failed")
        d.quit()                       
        
def item_to_invoice(d):
    try:
        time.sleep(1)
        newdeliverynote(d)
        time.sleep(1)
        print("Creating Item To Invoice")
        
        d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[1]/button").click()
        time.sleep(1)
        d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[1]/ul/li[3]/a").click()
        time.sleep(2)
        getcustname=d.find_element_by_xpath("//*[@data-fieldname='customer'] //*[@ data-doctype='Sales Invoice']").get_attribute('value')
    
        time.sleep(1)
        #print("cust name"+getcustname) 
        #print("Saving  Item To Invoice ")
        time.sleep(1)       
        d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
        time.sleep(4);                   
        fname1=d.find_element_by_xpath(".//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[1]/h1").text
        #print(" ---"+fname1)
        
        time.sleep(1)           
        if fname1==getcustname+" Draft":
            #print(" - Save Draft ")
            
            d.find_element_by_xpath("//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[2]/button[2]/span").click()
            time.sleep(2)             
            d.find_element_by_xpath("/html/body/div[34]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
        
        time.sleep(2)                     
        fname1=d.find_element_by_xpath(".//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[1]/h1").text
        #print("temp name "+fname1)
        time.sleep(3)
        if fname1==getcustname+" Unpaid":
            print("Item To Invoice Name :"+getcustname+" is created")
        
        print
        
    except:
        print("I_to_IV Failed")
        d.quit()