import calendar
from datetime import datetime
now=datetime.now()
trap=now.date()
uzi=list(str(trap))
trick=int(uzi[0]+uzi[1]+uzi[2]+uzi[3])
age=input('Enter your age: ')
trap=int(trick)-int(age)
month=input('Enter the month you were born: ')
date=input('Enter the date you were born: ')
cal=calendar.weekday(int(trap),int(month),int(date))
daysofweek=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
monthsofyear=['January','February','March','April','May','June','July','August','September','October','November','December']
print('You where born on ',daysofweek[cal],date, monthsofyear[int(month)-1], trap)

