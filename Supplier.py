import time
import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


supplier_name=("","Emp1","Testsupplier1")

supplier_type=("","sr","Raw Material")

def Supplierlist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Supplier List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Supplier List Page")
        time.sleep(2)
    except:
        print(" list Failed")
        d.quit()
        
def tocheckmsg(d):
    try:
        time.sleep(2)
        if d.find_element_by_class_name("msgprint").is_displayed():
            time.sleep(3);                          
            errors=d.find_element_by_class_name("msgprint").text            
            print("Errors :"+errors)
            time.sleep(3);
            d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
    except:
        print(" msg Failed")
        d.quit()   
        
   
def newsupplier(d):
    try:
        size=supplier_name.__len__()
        Supplierlist(d)
        time.sleep(2)
                                      
        if d.find_element_by_xpath(".//*[@id='page-List/Supplier']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Supplier']/div[1]/div/div/div[2]/button[2]").click()
            #print(" after new ")
            time.sleep(1)
            d.find_element_by_xpath("//button[text()='Edit in full page']").click()
            
            
        
            for i in range(size):    
                xsupplier_name="//*[@data-fieldname='supplier_name'] //*[@data-doctype='Supplier']"
                d.find_element_by_xpath(xsupplier_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xsupplier_name).send_keys(supplier_name.__getitem__(i))
                time.sleep(1)
                
                
                xsupplier_type="//*[@data-fieldname='supplier_type'] //*[@data-doctype='Supplier']"
                d.find_element_by_xpath(xsupplier_type).clear()
                time.sleep(1)
                d.find_element_by_xpath(xsupplier_type).send_keys(supplier_type.__getitem__(i))
                time.sleep(1)

                print("Saving  Supplier ")
               
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                time.sleep(4);                  
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Supplier']/div[1]/div/div/div[1]/h1").text
                #print(" ---"+fname1)
                temp=supplier_name.__getitem__(2)
                
                if fname1==temp+" Enabled":
                    print("Supplier Name :"+temp+" is created")
                else:
                    tocheckmsg(d)
                    print
                            
        
                
    except:
        print(" new Failed")
        d.quit()   
                        