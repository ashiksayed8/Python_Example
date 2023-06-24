#Ptyhon program to display all the prime numbers within an interval------------------


lower = 900
upper = 1000

print("prime numbers between", lower, "and", upper, "are: ") 

for num in range(lower, upper + 1):
    #all prime numbers are freater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) ==0:
                break
            else:
                print(num)
            