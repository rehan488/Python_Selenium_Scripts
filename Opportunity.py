import time
import re
import Utility
import Item
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

enquiry_from=("Lead","Lead","Lead")
gender=("","2","Male")
company_name=("","ewq","Indictrans")
leadname=("","sr","LEAD-00001")
custgroup=("","sr","Government")
email_id=("", "feb12","rehan@gmail.com")
pcustgroup=("","re","All Customer Groups")
source=("","emp","Walk In")

def opportunitylist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Opportunity List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Opportunity List Page")
        time.sleep(2)
        
        
    except:
        print("Failed")
        d.quit()

def tocheckmsg(d):
    try:
        time.sleep(2)
        if d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").is_displayed():            
            #print("Lead name ")
            time.sleep(2);                                                     
            countries=d.find_element_by_class_name("msgprint").text
            print(countries)
            time.sleep(1);           
            d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(1)
    except:
        print("Failed")
        d.quit()
        
def newopportunity(d):
    try:
        size=enquiry_from.__len__()
        time.sleep(2)
        opportunitylist(d)
        time.sleep(2)           
        if d.find_element_by_xpath(".//*[@id='page-List/Opportunity']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Opportunity']/div[1]/div/div/div[2]/button[2]").click()
            #print(" after new ")
    
            for i in range(size):    
                time.sleep(2)
                #//*[@data-fieldname='enquiry_from'] //*[@data-fieldtype='Select']
                xenquiry_from="//*[@data-fieldname='enquiry_from'] //*[@data-fieldtype='Select']"
                time.sleep(1)
                d.find_element_by_xpath(xenquiry_from).send_keys(enquiry_from.__getitem__(i))   
                
               
                time.sleep(2)
                xleadname="//*[@data-fieldname='lead'] //*[@data-doctype='Opportunity']"
                d.find_element_by_xpath(xleadname).clear()
                time.sleep(1)
                d.find_element_by_xpath(xleadname).send_keys(leadname.__getitem__(i))   
                
                xcompany_name="//*[@data-fieldname='company'] //input[@type='text']"
              
                if(i==2):
                    d.find_element_by_xpath(xcompany_name).click()
                    time.sleep(1)
                    d.find_element_by_xpath("//a[contains(@class, 'h6 uppercase') and text() = 'Source']").click()
                    time.sleep(1)
                     
                       
                d.find_element_by_xpath(xcompany_name).clear()
                xcompany_name="//*[@data-fieldname='company'] //input[@type='text']"
                d.find_element_by_xpath(xcompany_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xcompany_name).send_keys(company_name.__getitem__(i))
                                 
                
                
                print("Saving  Opportunity ")
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                time.sleep(6);                  
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Opportunity']/div[1]/div/div/div[1]/h1").text
                #print(" ---"+fname1)
                time.sleep(1);
                temp=company_name.__getitem__(2)
                #print("temp name "+temp)
                time.sleep(1);
                if fname1==temp+" Open":
                    print("Opportunity Name :"+temp+" is created")
                else:
                    tocheckmsg(d)
    
                print
    
    
    
    except:
        print("Failed")
        d.quit()



def Opportunity_Quotation(d):
    try:
        time.sleep(2)
        newopportunity(d)
        print("Creating Opportunity_Quotation ")
        time.sleep(2)
        if d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/button").is_displayed():
            #print("click on Make button ")
            time.sleep(2)
            d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/button").click()
            time.sleep(1)
            d.find_element_by_xpath("//*[@id='page-Form/Opportunity']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/ul/li/a").click() 
            time.sleep(2)
            
                                      
            d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[3]/div/div[1]/button[3]").click()
                    
                                      
            time.sleep(4)             
            d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[2]/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div[6]/div/div/form/div/div/div/div[2]/div[1]/div/div/div[2]").click()
            time.sleep(4)  
            d.find_element_by_xpath("//*[@data-fieldname='item_code'] //*[@ data-doctype='Quotation Item']").send_keys(Item.itemcode.__getitem__(2))
            time.sleep(1)   
            d.find_element_by_xpath("//*[@data-fieldname='qty'] //*[@ data-doctype='Quotation Item']").click()
            
            
            
            print("Saving  Opportunity_Quotation ")
            d.find_element_by_xpath("//*[@id='page-Form/Quotation']/div[1]/div/div/div[2]/button[2]/span").click()
            time.sleep(6);                  
            fname1=d.find_element_by_xpath(".//*[@id='page-Form/Quotation']/div[1]/div/div/div[1]/h1").text
            #print(" ---"+fname1)
            temp=company_name.__getitem__(2)
            
            if fname1==temp+" Draft":
            #print(" - Save Draft ")
            
                d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Submit']").click()
                time.sleep(2)             
                d.find_element_by_xpath("/html/body/div[21]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
                
                time.sleep(1);
                fname1=d.find_element_by_xpath(".//*[@id='page-Form/Quotation']/div[1]/div/div/div[1]/h1").text
                #print("temp name "+temp)
                time.sleep(1);
                if fname1==temp+" Submitted":
                    print("Opportunity_Quotation Name :"+temp+" is created")
                else:
                    tocheckmsg(d)
            
            print
    
    
    
    
    except:
        print("Failed")
        d.quit()

          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
     
     
     
        
        
        
        
        
        
        