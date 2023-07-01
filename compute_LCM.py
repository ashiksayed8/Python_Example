# Python Program to find the L.C.M of two input number

def compute_lcm(x, y):
#choose the greate number
    if x > y:
        greate = x
    else:
        greate = y
    while(True):
        if((greate % x == 0) and (greate % y) == 0):
            lcm = greate
            break
        greate += 1
        
num1 = 54
num2 = 24

print("The L.C.M", compute_lcm(num1,num2))
    