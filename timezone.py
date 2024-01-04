# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:33:24 2023

@author: Prathvish Shetty
"""

from datetime import datetime as dt
import pytz
timezones=pytz.all_timezones
for i in range(len(timezones)):
    zone=timezones[i]
    tz=pytz.timezone(zone)
    print("Current time at",zone,"is",dt.now(tz))