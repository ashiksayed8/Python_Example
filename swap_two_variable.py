""" #Python program to swap two variables

x = 5
y = 10

# To take inputs from the user

# x = input("Enter value of x: ")
# y = input("Enter value of y:")


#Create a temporary variable and swap the values

temp = x
x = y 
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y)) """





#without using temporary variable

""" x = 5
y = 10

x,y = y,x
print("x = ", x)
print("y = ", y) """



#Addition and subtraction 
x = 5
y = 6

""" x = x + y
y = x - y
x = x - y """

# Multiplication and division-------

x = x * y
y = x / y
x = x / y


#XOR swap -------

x = x ^ y
y = x ^ y
x = x ^ y
 
