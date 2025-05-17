#if, elif, and else are conditional statements that control the flow of execution
#if; executes a block of code if the specified condition is true
#if-else; provides an additional block of code if the condition is false
#if-elif-else ; Handles multiple conditions in a sequential order.

#logical operators are used to combine multiple conditions
#and checks if both conditions are true ex. ( 4 < x and x > 1) i.e true if both conditions are true.
#or checks both conditions to see if at least one is true, ( 4 < x or x > 1) i.e true if at least one condition is true
#not checks the condition and gives the inverse. ( not 5 > x), i.e true if x = or greater than 5)

age = int(input("What is your age? (Numerical Value): "))

if age < 18:
    print("You are a minor!")

elif age > 17 and age < 66:
    print("You are an adult!")

else:
    print("You are a senior!")