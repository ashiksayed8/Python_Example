num =1634

#Changed num variable to string.
# and calculated the lenght (number of digits)

order = len(str(num))


#initialize sum
sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
    
if num == sum:
    print(num, "is Armstrong number")
else:
    print(num, "is not Armstrong number")