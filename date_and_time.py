import datetime


class GetDate():
    
    def __init__(self):
        
        today = datetime.datetime.now()

        if today.month < 10:
            month = "0" + str(today.month)
        else:
            month = today.month
            
        if today.day < 10:
            day = "0" + str(today.day)
        else:
            day = today.day
            
        year = today.year

        self.today_date = "%s/%s/%s" % (month, day, year)
    
        if today.hour<12:
            self.am_or_pm = "am"
        else: 
            self.am_or_pm = "pm"