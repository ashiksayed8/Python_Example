# Program to display calender of the given month and year

# importing calender module 

import calendar

yy = 1996 #year

mm = 5 # month 

# To take month and year input from the user

#yy = int(input("Enter year: "))
#mm = int(input("Enter month: "))

#display the calender 

print(calendar.month(yy, mm))