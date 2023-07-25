# Define punctuation

punctuation = '''!()-[];:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user 
#my_str = input("Enter a string: ")

#Remove punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuation:
        no_punct = no_punct + char

#Display the unpunctuated string

print(no_punct)



