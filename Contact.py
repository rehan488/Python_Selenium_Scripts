import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

fname=("","Emp1","Test")
salutation=("", "asds","Mr")
lname=("","asd","personname")
email=("", "feb12","rehan@gmail.com")
fname=("","Emp1","Test")
gender=("","m","Male")
phone=("", "adasd12","114258210")
mobile=("","adbabf32","1234567890")

def contactlist(d):
    try:
        time.sleep(2)
        d.find_element_by_id("navbar-search").send_keys("Contact List")
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.DOWN)
        time.sleep(1)
        d.find_element_by_id("navbar-search").send_keys(Keys.ENTER)
        print("On Contact List Page")
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
            d.find_element_by_xpath("/html/body/div[9]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
            
        elif d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").is_displayed():
            #missfields=d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Missing Fields']").getText()
            print("contact name ")
            time.sleep(5);
            #byxpath = d.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[1]/ul/li")
            #List<WebElement> listElement = d.findElements(byxpath)
            #for(WebElement list: listElement)        
            countries=Select(d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[2]/div[1]/ul/li")).options
            for index, value in enumerate(countries):
                print("Mandatory fields required in Contact: "+value.text)
            time.sleep(5);            
            d.find_element_by_xpath("/html/body/div[10]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
            time.sleep(3)
    except:
        print("Failed")
        d.quit()
        
        
def newcontact(d):
    try:
        size=fname.__len__()
        time.sleep(2)
        contactlist(d)
        time.sleep(2)
        #=======================================================================
        # if d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Not found']").is_displayed():
        #     time.sleep(1)
        #     d.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()
        #     time.sleep(2)
        #=======================================================================
        if d.find_element_by_xpath(".//*[@id='page-List/Contact']/div[1]/div/div/div[2]/button[2]").is_displayed():
            #System.out.println(" found")
            time.sleep(1)
            d.find_element_by_xpath(".//*[@id='page-List/Contact']/div[1]/div/div/div[2]/button[2]").click()
            print(" after new ")

            for i in range(size):    
                time.sleep(2)
                xfirst_name="//*[@data-fieldname='first_name'] //input[@type='text']"
                d.find_element_by_xpath(xfirst_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xfirst_name).send_keys(fname.__getitem__(i))

                xlast_name="//*[@data-fieldname='last_name'] //input[@type='text']"
                d.find_element_by_xpath(xlast_name).clear()
                time.sleep(1)
                d.find_element_by_xpath(xlast_name).send_keys(lname.__getitem__(i))

                xsalutation="//*[@data-fieldname='salutation'] //input[@type='text']"
                d.find_element_by_xpath(xsalutation).clear()
                time.sleep(1)
                d.find_element_by_xpath(xsalutation).send_keys(salutation.__getitem__(i))

                xemail_id="//*[@data-fieldname='email_id'] //input[@type='text']"
                d.find_element_by_xpath(xemail_id).clear()
                time.sleep(1)
                d.find_element_by_xpath(xemail_id).send_keys(email.__getitem__(i))
                time.sleep(2)
                
                xgender="//*[@data-fieldname='gender'] //input[@type='text']"
                d.find_element_by_xpath(xgender).click()
                #print("Email validation ")
                regx="^[A-Za-z](.*)([@]{1})(.{1,})(\\.)(.{1,})"
                #^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$
                if re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email.__getitem__(i)):
                    #print("Message  Not display ")
                    time.sleep(1);
                    d.find_element_by_xpath(xgender).send_keys(gender.__getitem__(i))

                    xphone="//*[@data-fieldname='phone'] //input[@type='text']"
                    d.find_element_by_xpath(xphone).clear();
                    time.sleep(1);
                    d.find_element_by_xpath(xphone).send_keys(phone.__getitem__(i))
                    
                    xmobile_no="//*[@data-fieldname='mobile_no'] //input[@type='text']"
                    d.find_element_by_xpath(xmobile_no).clear()
                    time.sleep(1);
                    d.find_element_by_xpath(xmobile_no).send_keys(mobile.__getitem__(i))

                    print("Saving  Contact ")
                    d.find_element_by_xpath("//span[contains(@class, 'hidden-xs') and text() = 'Save']").click()
                    time.sleep(6);
                    fname1=d.find_element_by_xpath(".//*[@id='page-Form/Contact']/div[1]/div/div/div[1]/h1/div[2]").text
                    #print("Contact name ---"+fname1)
                    time.sleep(3);
                    temp=fname.__getitem__(2)+" "+lname.__getitem__(2)
                    #print("temp name "+temp)
                    time.sleep(3);
                    if fname1==temp:
                        print("Contact Name :"+fname1+" Contact is created")
                    else:
                        #print("else condition")
                        tocheckmsg(d)
                           
                elif email.__getitem__(i)=="":
                    print("Blank value  ")
                else:
                    #print("Message  display")
                    time.sleep(1);
                    if d.find_element_by_xpath("//h4[contains(@class, 'modal-title') and text() = 'Message']").is_displayed():
                        time.sleep(2);           
                        d.find_element_by_xpath("/html/body/div[9]/div[2]/div/div[1]/div/div[2]/div/button[1]/span").click()       
    except:
        print("Failed")
        d.quit()