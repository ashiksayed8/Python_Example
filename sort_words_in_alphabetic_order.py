# Program to sort alphabetically the words from a string

my_str = "Hello this Is an Example with caed letters"

# To take input from the user
# my_str = input("Enter a string: ")

#Break the string into a list of words 

words = [word.lower() for word in my_str.split()]

# Sort the list 

words.sort()

#Display the sortes words

print("The sorted words are: ")
for word in words:
    print(word)


