import time
import re
import Item
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

leadname=("","sr","Testperson")
gender=("","ma","Male")
company_name=("","ma","Indictrans")
opportunity=("","ma","Indictrans")
item_code=Item.itemcode
qty=("","r","2")
rate=("","r","10")


def leadlist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Lead List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Lead List Page")
        time.sleep(2)
    except:
        print("Failed")
        d.quit()
        
def newlead(d):
    try:
        leadlist(d)                 
        time.sleep(2)             
        d.find_element_by_xpath("//*[@id='page-List/Lead']/div[1]/div/div/div[2]/button[2]/span").click()
        time.sleep(2)
        d.find_element_by_xpath("//*[@data-fieldname='lead_name'] //*[@ data-doctype='Lead']").send_keys(leadname.__getitem__(2))
        time.sleep(2)
        d.find_element_by_xpath("//*[@data-fieldname='gender'] //*[@ data-doctype='Lead']").send_keys(gender.__getitem__(2))
        time.sleep(2)
        d.find_element_by_xpath("//*[@data-fieldname='company_name'] //*[@ data-doctype='Lead']").send_keys(company_name.__getitem__(2))
        time.sleep(2)
        d.find_element_by_xpath("//*[@id='page-Form/Lead']/div[1]/div/div/div[2]/button[2]/span").click()
        time.sleep(6);
        leadname1=d.find_element_by_xpath("//*[@id='page-Form/Lead']/div[1]/div/div/div[1]/h1").text
        print("Lead Created ---"+leadname1)
        
        
    except:
        print("Failed")
        d.quit()

def lead_customer(d):
    try:   
        newlead(d)   
        time.sleep(5);
        d.find_element_by_xpath("//*[@id='page-Form/Lead']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/button").click()
        time.sleep(3);
        d.find_element_by_xpath("//*[@id='page-Form/Lead']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/ul/li[1]/a").click()
        
        #creating opportunity from lead
        
        time.sleep(4);
        d.find_element_by_xpath("//*[@id='page-Form/Customer']/div[1]/div/div/div[2]/button[2]/span").click()
        time.sleep(2);
        custname1=d.find_element_by_xpath("//*[@id='page-Form/Customer']/div[1]/div/div/div[1]/h1").text
        if custname1==company_name.__getitem__(2) +" Enabled":
        
            print("Customer Created "+company_name.__getitem__(2))
        
        print
        
    except:
        print("Failed")
        d.quit()    
        
def lead_opportunity(d):
    try:
        time.sleep(2)
        newlead(d)  
        
        time.sleep(5)
        d.find_element_by_xpath("//*[@id='page-Form/Lead']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/button").click()
        time.sleep(3)
        d.find_element_by_xpath("//*[@id='page-Form/Lead']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/ul/li[2]/a").click()
        
        #creating customer from lead
        time.sleep(2)
        d.find_element_by_xpath("//*[@data-fieldname='company'] //*[@ data-doctype='Opportunity']").send_keys(company_name.__getitem__(2))
      
        time.sleep(4)           
        d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[1]/div/div/div[2]/button[2]/span").click()
        time.sleep(2)
        custname1=d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[1]/div/div/div[1]/h1").text
        if custname1==opportunity.__getitem__(2) +" Open":
        
            print("Opportunity Created " +opportunity.__getitem__(2))
        
        time.sleep(5)            
        d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/button").click()
        time.sleep(3)             
        d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/ul/li/a").click()
        time.sleep(6)            
        d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[3]/div/div[1]/button[3]").click()
        
        #click on add new row for items
        
        time.sleep(4)             
        d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[2]").click()
        time.sleep(4)  
        d.find_element_by_xpath("//*[@data-fieldname='item_code'] //*[@ data-doctype='Quotation Item']").send_keys(item_code.__getitem__(2))
        time.sleep(1)   
        d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Quotation Item']").click()
         
        time.sleep(1)    
        d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Quotation Item']").send_keys(Keys.CONTROL,'a')
        time.sleep(1)    
        d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Quotation Item']").send_keys(Keys.BACK_SPACE)
        time.sleep(1)    
        d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Quotation Item']").send_keys(qty.__getitem__(2))
        time.sleep(1)  
        d.find_element_by_xpath("//*[@data-fieldname='rate'] //*[@ data-doctype='Quotation Item']").clear()
        time.sleep(1)    
        d.find_element_by_xpath("//*[@data-fieldname='rate'] //*[@ data-doctype='Quotation Item']").send_keys(rate.__getitem__(2))
        
        
        time.sleep(3)             
        d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[1]/div/div/div[2]/button[2]/span").click()
        
        time.sleep(3)                       
        custname1=d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[1]/div/div/div[1]/h1").text
        if custname1==opportunity.__getitem__(2) +" Draft":
        
            print("Quotation  " +custname1)  
            time.sleep(2)      
            d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[1]/div/div/div[2]/button[2]").click()
            
        time.sleep(5)              
        
        
        #/html/body/div[50]/div[2]/div/div[1]/div/div[2]/div/button[2]
        if d.find_element_by_xpath("//button[text()='Yes']").is_displayed():
            d.find_element_by_xpath("//button[text()='Yes']").click()
            time.sleep(4)                                                  
            quotationname=d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[1]/div/div/div[1]/h1").text
            if custname1==opportunity.__getitem__(2) +" Draft":
                print("Quotation Created " +quotationname)  
    
               
    except:
        print("Failed")
        d.quit()






