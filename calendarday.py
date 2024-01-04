# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:26:13 2023

@author: Prathvish Shetty
"""

import calendar

def check_valid_date(dt,m,y,l):
    if l:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                    if m%2==0:
                        if dt<32:
                            return True
                        else:
                            return False
                    else:
                        if dt<31:
                            return True
                        else:
                            return False
                    
    else:
        if m==2:
            if dt<29:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m<8:
                    if m%2==0:
                        if dt<32:
                            return True
                        else:
                            return False
                    else:
                        if dt<31:
                            return True
                        else:
                            return False

def check_leap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True  
        else:
            return False

def get_day(day_index):
    list_of_days=["Monday","Tuesday","Wednesday","Thursday","Saturday","Sunday"]
    return list_of_days[day_index]
while(1):
    year=int(input("Enter year (1970+): "))
    if year<1970:
        print("Enter a year in the range 1970+")
    else:
        break;
while(1):
    month=int(input("Enter month (1-12): "))
    if month<1 or month>12:
        print("Enter a valid month in the range 1-12")
    else:
        break;
        
leap=check_leap(year)

while(1):
    date=int(input("Enter date: "))
    if check_valid_date(date,month,year,leap):
        break
    else:
        print("Enter a valid date")
        
day_index=calendar.weekday(year,month,date)
day=get_day(day_index)

print(date,'/',month,'/',year,"falls on",day)