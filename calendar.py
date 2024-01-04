# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:30:26 2023

@author: Prathvish Shetty
"""

from datetime import datetime as dt
print(dt.now())

import pytz

tz=pytz.timezone('Singapore');
print(dt.now(tz))

pytz.all_timezones


import calendar
#calendar.weekday?
calendar.weekday(2023,10,24)
Out[16]: 1