""" # Program to check if a number is prime or not--------

num = 28

# To take input from the user-----
# num = int(input("Enter a number: "))
# define  a flag variable -----
flag = False

if num == 1:
    print(num, "is not prime number")
elif num > 1:
    #check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to tru
            flag = True
            #break out of loop
            break
    # check if flag is True---------
    
    if flag:
        print(num, "is not prime number")
    else:
        print(num, "is a prime number") """
        
        
        
num = 407

# To take input from the user
#num = int(inpput("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    #check for factors
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
        else:
            print(num, "is a prime number")
# if input number is less than
# or equal to 1, it is not prime

else:
    print(num, "is not a prime number")