#Taking kilometers input from the user-------

# kilometers  = float(input("Enter value is kilometrs: "))

# #Conversion factor-----------
# conv_fac = 0.621371

# #Calculate miles--------
# miles  = kilometers * conv_fac
# print('%0.2f kilometers is equal to %0.2f miles' %(kilometers, miles))

#Convert miles to kilometers---------------
miles  = float(input("Enter value in miles: "))

# Conversion factor
conv_fac = 0.621371

#Calculate  kilometers------
kilometers = miles / conv_fac
print('%0.2f miles is equal to % 0.2f kilometers' %(miles, kilometers))


