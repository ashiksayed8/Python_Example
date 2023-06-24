# Program to check if a number is prime or not--------

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
        print(num, "is a prime number")