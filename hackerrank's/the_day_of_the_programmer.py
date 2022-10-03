def is_leap_year(n):
    if n >1919:
        return True if  n%400==0 or (n%4==0 and n%100!=0) else False
    else: 
        return True if n%4==0  else False

def dayOfProgrammer(year):
    if year==1918:
        return "26.09.1918"
    if is_leap_year(year):
        return f"{256-244}.09.{year}"
    else: 
        return f"{256-243}.09.{year}"