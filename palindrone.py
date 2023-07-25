# Program to check if a string is palindrone or not 


my_str = 'aIbonPhoBiA'

# make it suitable for caseless comparion  


my_str = my_str.casefold()

#reverse the string 

rev_str = reversed(my_str)

# check if the string is equal to its reverse 

if list(my_str) == list(rev_str):
    print("The string is a palindrone")
else:
    print("The string is not a palindrome")
    