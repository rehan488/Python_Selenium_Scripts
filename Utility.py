'''
Created on Jan 22, 2018
Utility
@author: indic
'''

from datetime import datetime as DateTime, timedelta as TimeDelta

def nextdate():
    try:

            date_1 = DateTime.today() 
                
            end_date = date_1 + TimeDelta(days=10)
            
            qdate=end_date.strftime("%d-%m-%Y")
            
            #print(qdate)
            
            return qdate
    except:
        print("Failed")
        
        
nextdate()