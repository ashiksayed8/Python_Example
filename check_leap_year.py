# Python program to check if year is a leap year or not 

year = 2003

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

#Divided by 100 means century year(Ending with 00)
#century year divided by 400 is leap year-----------

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

#Not divided by 100 means not a century year
#year divided by 4 is a leap year 
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
#if not divided by both 400(century year) and 4 (not century year)
#Year is not leap year----------
else:
    print("{0} is not a leap year".format(year))
    
