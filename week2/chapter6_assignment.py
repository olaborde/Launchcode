def is_leap(year):
    century = year % 100 == 0
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and not century:
        return True
    else:
        return False
    
  

is_leap(1900)   