import unittest
from selenium import webdriver
import time
#from Contact import newcontact
#from Customer import newcustomer
#------------------------------------------------------ from Lead import newlead
#---------------------------------------- from Opportunity import newopportunity
#--------------------------------- from Opportunity import Opportunity_Quotation
#------------------------------------------------------ from Item import newitem
#------------------------------------------------ import salesorderfromquotation
#-------------------------------------------- from Quotation import newquotation
#--------------------------------------------------------------- import Flow_CRM
import DeliveryNote
import Supplier
import Purchase_Order



urlver10="http://localhost:8000"
username="administrator"
pwd="admin"
d=webdriver.Chrome(executable_path="/home/indic/Documents/rehan/selenium data/chromedriver")
       
def loginfun():

    try:   
        d.get(urlver10)
        d.maximize_window()
        time.sleep(1)
        d.find_element_by_id("login_email").send_keys(username)
        d.find_element_by_id("login_password").send_keys(pwd)      
        d.find_element_by_xpath(".//*[@id='page-login']/div/div/div[2]/section[1]/div[1]/form/button").click() 
        time.sleep(2)
        url=d.title
        
        if url=="Desktop":
            print("Login Sucessfully")
            time.sleep(1)
            if d.find_element_by_class_name("modal-title").is_displayed():
                time.sleep(2)
                d.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[1]").click()
                time.sleep(5)
                
    except:
        print("Login Failed")
        d.quit()
        
loginfun()
#newcustomer(d)
#newcontact(d)
#newlead(d)
#newopportunity(d)
#Opportunity_Quotation(d)
#newitem(d)
#Flow_CRM.lead_customer(d)
#Flow_CRM.lead_opportunity(d)
#createso(d)
#salesorderfromquotation.createSinvoice(d)
#salesorderfromquotation.createSOdelivery(d)
#newquotation(d)
#DeliveryNote.newdeliverynote(d)
#DeliveryNote.item_to_invoice(d)
#Supplier.newsupplier(d)
#Purchase_Order.newpurchase_order(d)
Purchase_Order.purchase_od_invoice(d)



time.sleep(4)
d.quit()

