# Pyhron program to find the sum of natural using recusion


def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n - 1)
    
# change this value for a differnt result 

num = 16

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))