my_str = "Hello, World!"
my_str_1 = 'Bye Bye World!'

my_multiline_str = '''
hello world
see you world
bye bye world
'''

print(my_str[0:])

#last character always

print(my_str[-1])


for i in my_str:
    print(i)

my_longer_str = '''
i want to graduate and i want to live 
near the beach i want to have my own beach house
with my small shop near there
'''
# the len function will show the number of character in a string
print(len(my_longer_str))

# checking if the word "or" is inside the phase "Hello, World"

print("or" in my_str)

print(my_str.upper())
print(my_str.lower())

#to delete the white block

my_str = " Hello, World "

print(my_str.strip())

# To replace the word

print(my_str.replace("Hello", "Bye Bye"))

# Mark where you want to split, can make it into a list (comma is the separator)

print(my_str.split(","))

# adding two string together

str_one = "Hello"
str_two = "World"

print(str_one + str_two)

print(str_one + " " + str_two)

# format string

print(f"tharoth, {str_two}")

# my name is i'm here
print('my name is i\'m here')

