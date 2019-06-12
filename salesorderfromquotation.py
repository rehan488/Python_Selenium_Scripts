import time
import re
from Utility import nextdate
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from datetime import datetime as DateTime, timedelta as TimeDelta



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
        print("Failed")
        d.quit()
    
def createso(d):
    try:
        quotationlist(d)
        time.sleep(2)
        if d.find_element_by_class_name("frappe-list-area").is_displayed():
            print("Table view ")
            listitem=d.find_element_by_class_name("list-item-container").text
            alllistitem=d.find_element_by_class_name("list-items").text
            alltemp='',alllistitem
            alllist1=alltemp[1].split("\n")
           
            qtitle=alllist1[0]
            
            size=alllist1.__len__()
            #===================================================================
            # date_1 = DateTime.today() 
            #     
            # end_date = date_1 + TimeDelta(days=10)
            # 
            # qdate=end_date.strftime("%d-%m-%Y")
            #===================================================================
            #print(alllist1)
            for i in range(3,size,6):
                qtitle=alllist1[i-3]
                qcode=alllist1[i]
               
                #print(qcode+"   "+qtitle)
                
                time.sleep(2)
                d.find_element_by_xpath("//*[@data-name='"+qcode+"' and contains(@class, 'grey list-id  ellipsis')]").click()
                time.sleep(3)
               
                d.find_element_by_xpath("//button[contains(@class, 'btn dropdown-toggle btn-xs btn-primary')]").click()
                time.sleep(2)
                d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/ul/li[1]/a").click()
                time.sleep(2)
                d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[3]").click()
                time.sleep(2)

                d.find_element_by_xpath("//*[@data-fieldname='delivery_date'] //*[@ data-doctype='Sales Order Item']").send_keys(nextdate())

                time.sleep(2)
                d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div[1]/div[7]/a/span").click()
                time.sleep(1)
                d.find_element_by_xpath("//*[@data-fieldname='warehouse'] //*[@ data-doctype='Sales Order Item']").clear()
                time.sleep(1)
                d.find_element_by_xpath("//*[@data-fieldname='warehouse'] //*[@ data-doctype='Sales Order Item']").send_keys("Stores - I")
                time.sleep(2)                
                
                time.sleep(2)
                #d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button[1]/span").click()
                d.find_element_by_xpath("//*[@data-fieldname='warehouse'] //*[@ data-doctype='Sales Order Item']").send_keys(Keys.ESCAPE)
                time.sleep(2)
                #save
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()

                time.sleep(2)
                d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[1]/div/div/div[2]/button[2]/span").click()
                time.sleep(5)                                      
                d.find_element_by_xpath("//button[contains(@class,'btn btn-primary btn-sm') and text()='Yes']").click()
                
                
                
                #d.find_element_by_xpath("//*[@id='navbar-breadcrumbs']/li[2]/a").click()
                time.sleep(4)
                if d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[1]/div/div/div[1]/h1").is_displayed():
                    soname= d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[1]/div/div/div[1]/h1").text
                    print("Sales Order created "+soname)
                    if qtitle+" To Deliver and Bill"==soname:
                        break
                #quotationlist(d)            
        else:
            print("table not view")

    except:
        print("Failed")
        d.quit()


def createSinvoice(d):
    try:
       
        time.sleep(2)
        createso(d)
        print("Creating Sales Invoice")
        time.sleep(2)
        d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()
        time.sleep(2)
        d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/a").click()
        time.sleep(5)
       
        
        d.find_element_by_xpath("//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[2]/button[2]/span").click()
        
        time.sleep(2)
        salesinvoicename=d.find_element_by_xpath("//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[1]/h1").text
        #print("salesinvoicename "+salesinvoicename);
        time.sleep(4)
        #save
        d.find_element_by_xpath("//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[2]/button[2]/span").click()
        time.sleep(4)                                   
        d.find_element_by_xpath("/html/body/div[37]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
        #print(" Confirm ")     
        time.sleep(5)                                     
        upsalesinvoicename=d.find_element_by_xpath("//*[@id='page-Form/Sales Invoice']/div[1]/div/div/div[1]/h1").text
        print("sales Invoice "+upsalesinvoicename);
    
    
    except:
        print("Failed")
        d.quit() 
        
        
def createSOdelivery(d):
    try:
       
        time.sleep(2)
        createso(d)
        print
        print("Creating Sales Order to Delivery")
        time.sleep(2)
        d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()
        time.sleep(2)             
        d.find_element_by_xpath("//*[@id='page-Form/Sales Order']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a").click()
        time.sleep(5)
       
                                  
        d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[1]/div/div/div[2]/button[2]/span").click()
        
        time.sleep(2)
        salesinvoicename=d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[1]/div/div/div[1]/h1").text
        #print("salesinvoicename "+salesinvoicename);
        time.sleep(4)
        #save
        d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[1]/div/div/div[2]/button[2]/span").click()
        time.sleep(4)                                   
        d.find_element_by_xpath("/html/body/div[37]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
        #print(" Confirm ")     
        time.sleep(5)                                               
        upsalesinvoicename=d.find_element_by_xpath("//*[@id='page-Form/Delivery Note']/div[1]/div/div/div[1]/h1").text
        print("created Sales Order to Delivery "+upsalesinvoicename);
    
    
    except:
        print("Failed")
        d.quit()                 
        
        