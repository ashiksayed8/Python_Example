# Python program to find the L.C.M of two input number


# This function computes GCD

def computes_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
#This function computes LCM 

def computes_lcm(x, y):
    lcm = (x*y)//computes_gcd(x, y)
    return lcm

num1 = 54
num2 = 24


print("The L.C.M is", computes_lcm(num1, num2))