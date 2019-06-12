import time
import re
import Utility
import Item
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


supplier_name=("","Emp1","Testsupplier1")

supplier_type=("","sr","Raw Material")

def purchase_orderlist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Purchase Order List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Purchase Order List Page")
        time.sleep(2)
    except:
        print(" list Failed")
        d.quit()
        
def tocheckmsg(d):
    try:
        time.sleep(1)
        if d.find_element_by_class_name("msgprint").is_displayed():
            time.sleep(1);                          
            errors=d.find_element_by_class_name("msgprint").text            
            print("Errors :"+errors)
            time.sleep(1);          
            d.find_element_by_xpath("/html/body/div[16]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(1)
    except:
        print(" msg Failed")
        d.quit()   
        
   
def newpurchase_order(d):
    try:
        size=supplier_name.__len__()
        purchase_orderlist(d)
        time.sleep(2)
                                      
        if d.find_element_by_xpath(".//*[@id='page-List/Purchase Order']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Purchase Order']/div[1]/div/div/div[2]/button[2]").click()
            #print(" after new ")
            time.sleep(1)
            
            
            
        
            for i in range(size):    
                xsupplier_name="//*[@data-fieldname='supplier'] //*[@data-doctype='Purchase Order']"
                d.find_element_by_xpath(xsupplier_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xsupplier_name).send_keys(supplier_name.__getitem__(i))
                
                
                #click on add new row for items
                
                
                if i==2:
                    time.sleep(2)             
                    d.find_element_by_xpath("//*[@id='page-Form/Purchase Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[7]/div/div/form/div[1]/div/div/div[2]/div[3]/div/div[1]/button[3]").click()
                    time.sleep(2) 
                    
                                              
                    d.find_element_by_xpath("//*[@id='page-Form/Purchase Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[7]/div/div/form/div[1]/div/div/div[2]/div[1]/div/div/div[2]").click()
                    time.sleep(2)  
                    d.find_element_by_xpath("//*[@data-fieldname='item_code'] //*[@ data-doctype='Purchase Order Item']").send_keys(Item.itemcode.__getitem__(2))
                    time.sleep(1)  
                    
                    d.find_element_by_xpath("//*[@data-fieldname='schedule_date'] //*[@ data-doctype='Purchase Order Item']").clear()
                     
                    time.sleep(2)  
                    d.find_element_by_xpath("//*[@data-fieldname='schedule_date'] //*[@ data-doctype='Purchase Order Item']").send_keys(Utility.nextdate())
                    time.sleep(1)   
                    d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Purchase Order Item']").click()
                     
                    time.sleep(1)    
                    d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Purchase Order Item']").send_keys(Keys.CONTROL,'a')
                    time.sleep(1)    
                    d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Purchase Order Item']").send_keys(Keys.BACK_SPACE)
                    time.sleep(1)    
                    d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Purchase Order Item']").send_keys(Item.qty.__getitem__(2))
                    
                    
                    time.sleep(1)  
                    d.find_element_by_xpath("//*[@data-fieldname='rate'] //*[@ data-doctype='Purchase Order Item']").click()
                    
                    time.sleep(1)  
                    d.find_element_by_xpath("//*[@data-fieldname='rate'] //*[@ data-doctype='Purchase Order Item']").send_keys(Keys.CONTROL,'a')
                    time.sleep(1)   
                    d.find_element_by_xpath("//*[@data-fieldname='rate'] //*[@ data-doctype='Purchase Order Item']").send_keys(Keys.BACK_SPACE)
                    time.sleep(1)    
                    d.find_element_by_xpath("//*[@data-fieldname='rate'] //*[@ data-doctype='Purchase Order Item']").send_keys(Item.rate.__getitem__(2))
                    
                    
                
                
                print("Saving  Purchase Order ")
               
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                time.sleep(4);                  
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Purchase Order']/div[1]/div/div/div[1]/h1").text
                #print(" ---"+fname1)
                temp=supplier_name.__getitem__(2)
                
                if fname1==temp+" Draft":
                    
                    d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Submit']").click()
                    time.sleep(2)             
                    d.find_element_by_xpath("/html/body/div[17]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
                
                time.sleep(1)
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Purchase Order']/div[1]/div/div/div[1]/h1").text
                #print("temp name "+fname1)
                time.sleep(2)
                if fname1==temp+" To Receive and Bill":
                    print("Purchase Order Name :"+temp+" is created")
                else:
                    tocheckmsg(d)
                    print
                
    except:
        print(" new Failed")
        d.quit()   


def purchase_od_invoice(d):
    
    try:
        time.sleep(1)
        newpurchase_order(d)
        print
        print("purchase_order_invoice")
        time.sleep(3)
        d.find_element_by_xpath("//*[@id='page-Form/Purchase Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()
        time.sleep(1)                   
        d.find_element_by_xpath("//*[@id='page-Form/Purchase Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/ul/li[2]/a").click()
        time.sleep(4)
        
                                 
        d.find_element_by_xpath(".//*[@id='page-Form/Purchase Invoice']/div[1]/div/div/div[2]/button[2]").click()
        time.sleep(4);                  
        fname1=d.find_element_by_xpath(".//*[@id='page-Form/Purchase Invoice']/div[1]/div/div/div[1]/h1").text
        #print(" ---"+fname1)
        temp=supplier_name.__getitem__(2)
        time.sleep(2);         
        if fname1==temp+" Draft":
            
            d.find_element_by_xpath("//*[@id='page-Form/Purchase Invoice']/div[1]/div/div/div[2]/button[2]/span").click()
            time.sleep(2)             
            d.find_element_by_xpath("/html/body/div[28]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
        
        time.sleep(1)
        fname1=d.find_element_by_xpath(".//*[@id='page-Form/Purchase Invoice']/div[1]/div/div/div[1]/h1").text
        #print("temp name "+fname1)
        time.sleep(2)
        if fname1==temp+" Unpaid":
            print("purchase_od_invoice Name :"+temp+" is created")
        else:
            tocheckmsg(d)
            print
            
            
    except:
        print(" purchase_od_invoice Failed")
        d.quit()   
    









                        