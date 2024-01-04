import random
import datetime
birthday=[]
i=0
while i<50:
    year=random.randint(1890,2023)
    if (year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1,12)
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)       
    dd=datetime.date(year,month,day)
    dayOFyear=dd.timetuple().tm_yday
    i=i+1
    birthday.append(dayOFyear)
birthday.sort()
i=0
while i<50:
    print(birthday[i])
#for d in birthday:
 #   print(d)