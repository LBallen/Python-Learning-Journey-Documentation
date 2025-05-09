#Type conversion changes a data type of a value
#Can be done implicitly or explicitly by manual user input
#This is fundamental; ensures that operations between different data types work correctly
#int() converts data into an integer
#float() converts data into a float value
#str() converts data into a string
#bool() converts data into boolean
#list() converts data into a list
#tuple() converts data into a tuple
#set() converts data into a set
#dict() converts data to a dictionary from key-value pairs ;
#dict([("a",1),("b",2]) -> {'a' : 1 , 'b': 2}
#complex() converts to a complex number;
#complex(1,2) -> (1+2j)
#converting data from a float to an int will cause data loss!!!

a = 1
b = 2
c = 3

result = a + b + c
print(result)
print(type(result))
#result is an int that = 6

a = 1.0
b = 2.0
c = 3.0
result = a + b + c
print(result)
print(type(result))
#result is a float that = 6.0

#here since I am typing a singular value in the first set of directions python implicitly defines these values as integers
#In the second set of directions I type an integer followed by a decimal point or a float value
#python recognizes this as a float value and implicitly converts the data accordingly
#I could manually do this to make the code more defined like in C

a = 1
b = 2
c = 3
a,b,c =int(a),int(b),int(c)
result = a + b + c
print(result)
print(type(result))
#result is an int that = 6

a = 1.0
b = 2.0
c = 3.0
a,b,c = float(a),float(b),float(c)
result = a + b + c
print(result)
print(type(result))
#result is a float that = 6.0

# This is explicit type conversion

#------------------------------------------------------------------------------------------------------

#A set is an unordered collection of unique elements. You may add or remove items, but it does not allow for duplicate values

variables = {"a","b","c"}
print(variables)
print(type(variables))
print(type(a))
#data type remains a float, printing the set with " " will print the variable, not the value

variables_value = {a ,b ,c}
print(variables_value)
print(type(variables_value))

c = b
variables_value = {a ,b ,c}
print(variables_value)
print(type(variables_value))

#converting a a list of duplicate values will eliminate the duplicates

#remember that this set is unordered

#for an ordered set we want a tuple
#you cannot change the elements of a tuple once made
#a tuple can contain duplicates

variables = (a ,b ,c)
x = variables[0]
y = variables[1]
z = variables[2]

print(x,y,z)
print(type(variables))

#A dictionary is an unordered collection of key-value pairs
#key value pairs map a key to a value
#dictonaries are mutable
#keys are unique and must not be duplicates
#keys must be immutable
c = 3
variables = {"a": a,"b":b,"c":c}
print(variables["a"])
print(variables["b"])
print(variables["c"])
variables["d"] = 4
variables["b"] = "unknown constant"
print(variables)
print(type(variables))

#can be str, int, flt

del variables["d"]
print(variables)