import time
import re
import Utility

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

leadname=("","Emp1","TestLead1")
gender=("","2","Male")
company_name=("","ewq","Indictrans")
custgroup=("","sr","Government")
email_id=("", "feb12","rehan@gmail.com")
pcustgroup=("","re","All Customer Groups")
source=("","emp","Walk In")


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

def tocheckmsg(d):
    try:
        time.sleep(2)
        if d.find_element_by_class_name("msgprint").is_displayed():
            already=d.find_element_by_class_name("msgprint").text
            print(already)            
            d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(2)
        elif d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").is_displayed():            
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
        
        
def newlead(d):
    try:
        size=leadname.__len__()
        time.sleep(2)
        leadlist(d)
        time.sleep(2)
        if d.find_element_by_xpath(".//*[@id='page-List/Lead']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Lead']/div[1]/div/div/div[2]/button[2]").click()
            #print(" after new ")
    
            for i in range(size):    
                time.sleep(2)
                xlead_name="//*[@data-fieldname='lead_name'] //input[@type='text']"
                d.find_element_by_xpath(xlead_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xlead_name).send_keys(leadname.__getitem__(i))

               

                xcompany_name="//*[@data-fieldname='company_name'] //input[@type='text']"
                d.find_element_by_xpath(xcompany_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xcompany_name).send_keys(company_name.__getitem__(i))
        
                xemail_id="//*[@data-fieldname='email_id'] //input[@type='text']"
                d.find_element_by_xpath(xemail_id).clear()
                time.sleep(1)
                d.find_element_by_xpath(xemail_id).send_keys(email_id.__getitem__(i))
                
                xgender="//*[@data-fieldname='gender'] //input[@type='text']"
                                            
                d.find_element_by_xpath(xgender).click()
                time.sleep(3)
                #print("Email validation ")
                regx="^[A-Za-z](.*)([@]{1})(.{1,})(\\.)(.{1,})"
                #^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$
                if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email_id.__getitem__(i)):
                    #print("Message  Not display ")
                    time.sleep(1);
                    d.find_element_by_xpath(xgender).send_keys(gender.__getitem__(i))
                
                    xsource="//*[@data-fieldname='source'] //input[@type='text']"
                    d.find_element_by_xpath(xsource).clear()
                    time.sleep(1)
                    d.find_element_by_xpath(xsource).send_keys(source.__getitem__(i))
                    
                    xcontact_date="//*[@data-fieldname='contact_date'] //input[@type='text']"
                    d.find_element_by_xpath(xcontact_date).clear()
                    time.sleep(1)
                    d.find_element_by_xpath(xcontact_date).send_keys(Utility.nextdate())
                    
                    xcontact_by="//*[@data-fieldname='contact_by'] //input[@type='text']"
                    d.find_element_by_xpath(xcontact_by).clear()
                    time.sleep(1)
                    d.find_element_by_xpath(xcontact_by).send_keys(Keys.ENTER)
                
                
                
                    print("Saving  Lead ")
                    d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                    time.sleep(6);                  
                    fname1=d.find_element_by_xpath(".//*[@id='page-Form/Lead']/div[1]/div/div/div[1]/h1").text
                    #print(" ---"+fname1)
                    time.sleep(1);
                    temp=leadname.__getitem__(2)
                    #print("temp name "+temp)
                    time.sleep(1);
                    if fname1==temp+" Lead":
                        print("Lead Name :"+fname1+" is created")
                    else:
                        #print("else condition")
                        tocheckmsg(d)
                elif email_id.__getitem__(i)=="":
                    print("Blank value  ")
                else:
                    print("Message  display")
                    time.sleep(1);
                    if d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Message']").is_displayed():
                        time.sleep(2);           
                        d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()     
            
            
    
    except:
        print("Failed")
        d.quit()
        
