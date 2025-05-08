# Using Variable Concatenation
# name = input("What is your name?")
# print("Hi " +name+ "!")
# age = input("How old are you?")
# print("Heyo, you are " +age+ " years old!")

#This does not take into account that the string age should be represented as an integer
#Also, using the + operator to join strings is not ideal
#If I tried to add a string + and set age as an integer, I would receive an error

#using a formatted string literal is ideal as it allows me to input variables and expressions directly into the string
#you do this by putting a **f** before a string i.e f"... "

# name = input("What is your name?")
# print(f"Hi, {name} !")
#
# age = int(input("How old are you?"))
# print(f"Heyo, you are {age} years old!")
# print(f"In 10 years, you will be {age+10} years old")

#However, What if I type an age that is not a number like twenty? or rubbish?
#The except block catches errors like this inside a try block.

# name = input("What is your name?")
# print(f"Hi, {name} !")
#
# try:
#     age = int(input("How old are you?"))
#     print(f"Heyo, you are {age} years old!")
#     print(f"In 10 years, you will be {age+10} years old")
#
# except ValueError:
#     print("Looks like you did not enter a number.")

#Now, I'll add a way to convert a string like twenty into a number.
#This is a small dive into if and else and calling functions from libraries
#I could be very inefficient and use definitions by creating a function like
#convertword =
# {
#     'one' = 1
#     'Two' = 2
#     ...
#     'one hundred and 20' = 120
# }
#However, I will be calling a function 'word_to_num' from the class 'w2n' from the library 'word2number'
#I am going to renaming the class as something that I like better such as convert

#pip install word2number into terminal

from word2number import w2n as convert

name = input("What is your name?: ")
print(f"Hi, {name} !")

try:
    age_input = input("How old are you? (Word or number): ")
    age = convert.word_to_num(age_input)
    if age > 120:
        print("Sorry, I didn't realize I was talking to a vampire.")
    elif age < 120:
        print(f"Heyo, you are {age} years old!")
        print(f"In 10 years, you will be {age+10} years old")
except ValueError:
    print("Looks like you did not enter a number.")


