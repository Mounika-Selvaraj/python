def is_leap(year):
    leap = False
    if year%4==0:
        if year%400==0 or year%100==0:
            leap=true
    return leap
year = int(input())
