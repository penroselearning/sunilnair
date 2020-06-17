from datetime import datetime,timedelta
import calendar
import math
from fractions import Fraction


def calc_square(number):
    return number**2

def convert_to_seconds(y,mo,w,d,h,m):
  seconds =(m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60) + (w * 7 * 24 * 60 * 60) + (mo * 30 * 7 * 24 * 60 * 60) + (y * 52 * 7 * 24 * 60 * 60)
  return seconds

def birthday_countdown(birthdate):
    today = datetime.now()
    current_year = today.strftime('%Y')

    birth_year = int(birthdate[0:4])
    birth_month = int(birthdate[5:7])
    birth_day = int(birthdate[8:])

    date = datetime.strptime(f"{birth_day}-{birth_month}-{birth_year}",'%d-%m-%Y')
    first_date = (f"{birth_day}-{birth_month}-{current_year}")

    birth_date = datetime.strptime(first_date,'%d-%m-%Y')

    if birth_date > today:
      n = (birth_date - today)
      countdown = n.days, n.seconds//3600
    else:
      n = (birth_date+timedelta(days=365) - today)
      countdown = n.days, n.seconds//3600


    new_date=[]
    d=0
    current_year = int(current_year)
    for x in range(5):
      if calendar.isleap(current_year+(x+1)):
        d += 366
      else:
        d += 365
        
      next_five_yrs = birth_date + timedelta(days=d)
      new_date.append(next_five_yrs.strftime('%A-%Y'))


    return countdown,new_date

def aspect_ratio_calculator(w,h,nw,nh):
    
    try:
        f = Fraction(w,h)
    except:
        ratio = (0,0)
    else:
        ratio = f.numerator,f.denominator
    
    if nw == 0:
        try:
            nw = (nh/h) * w
        except:
            nw=0
    elif nh == 0:
        try:
            nh = (nw/w) * h
        except:
            nh=0
    return w,h,nw,nh,ratio