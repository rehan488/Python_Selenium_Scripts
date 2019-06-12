import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import Item

quoname=("","Emp1","Testcust1")

leadname=("","sr","LEAD-00007")



def quotationlist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Quotation List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Quotation List Page")
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
        
        
        
        
def newquotation(d):
    try:
        size=quoname.__len__()
        quotationlist(d)
        time.sleep(2)
        
        if d.find_element_by_xpath(".//*[@id='page-List/Quotation']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Quotation']/div[1]/div/div/div[2]/button[2]").click()
            #print(" after new ")
        
            for i in range(size):    
        
        
                xquoname="//*[@data-fieldname='customer'] //*[@data-doctype='Quotation']"
                #d.find_element_by_xpath(xquoname).clear()
                time.sleep(1)
                d.find_element_by_xpath(xquoname).send_keys(quoname.__getitem__(i))
                if i==2:
                    d.find_element_by_xpath(xquoname).send_keys(Keys.ENTER)
                    time.sleep(1)
                    d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[3]/div/div[1]/button[3]").click()
                    
                    time.sleep(4)             
                    d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[2]").click()
                    time.sleep(4)  
                    d.find_element_by_xpath("//*[@data-fieldname='item_code'] //*[@ data-doctype='Quotation Item']").send_keys(Item.itemcode.__getitem__(i))
                    time.sleep(1)   
                    d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Quotation Item']").click()



                print("Saving  Quotation ")
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                time.sleep(6);                  
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Quotation']/div[1]/div/div/div[1]/h1").text
                #print(" ---"+fname1)
                temp=quoname.__getitem__(2)
                
                if fname1==temp+" Draft":
                    #print(" - Save Draft ")
                    
                    d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Submit']").click()
                    time.sleep(2)             
                    d.find_element_by_xpath("/html/body/div[17]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
                
                time.sleep(1);
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Quotation']/div[1]/div/div/div[1]/h1").text
                #print("temp name "+temp)
                time.sleep(1);
                if fname1==temp+" Submitted":
                    print("Quotation Name :"+temp+" is created")
                else:
                    tocheckmsg(d)
    
                print
        
    except:
        print("new Failed")
        d.quit()                