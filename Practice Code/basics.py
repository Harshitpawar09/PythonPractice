'''print("Hello MindCoders")
#How Are You Doing?
Name - Harshit
Branch - AIML
College - IPS Academy Indore
age = 4
print(age)
name = "Harshit"
profession = "AIML Engineer"
experience = 1
print("Hello, I am", name, ". I am a", profession, "professionally .And I have around", experience, "year of experience with it.")



Data Types in Python:

text-str
numeric-int, float, complex
sequence-list, tuple, range
mapping-dict
set-set, frozenset
boolean-bool
binary-bytes, bytearray, memoryview
none-none

#########

x = 5
print(type(x))
x = "Hello World"
print(x)
print(type(x))
x = 20
print(x)
print(type(x))
x = 20.5
print(x)
print(type(x))
x = 1 + 2j
print(x)
print(type(x))
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
x = ("apple", "banana", "cherry")
print(x)
print(type(x))
x = range(6)
print(x)
print(type(x))
x = {"name" : "John", "age" : 36}
print(x)
print(type(x))
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = b"Hello"
print(x)
print(type(x))
x = bytearray(5)
print(x)
print(type(x))
x = memoryview(bytes(5))
print(x)
print(type(x))
x = None
print(x)
print(type(x)) '''


#####
'''
x = 4
print(x < 5 and x < 10)
print(x > 5 or x > 10)
print(x > 3 or x > 10)
print(not(x > 3 or x > 10))

x = 10
y = 10
print(x is y)


#######
x = ["Maruti", "BMW"]
y = ["Maruti", "BMW"]
z = x
print(x is y)
print(x is z)
print(x is not y)
print(x is not z)


####
y = ["Maruti", "BMW"]
x = "Maruti"
print(x in y)
print(x not in y)  

#########
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
print("Hello", name,)
print("Your Age is", age)

x = input("Enter a number for sum: ")
y = input("Enter another number for sum: ")
z = int(x) + int(y) #typecasting
print("The sum is:", z)



print("*" * 10)
print("+"+"-"*10+"+")
print("|" + " "*10 + "|")
print(("|" + " "*10 + "|\n")*5, end="")
print("+"+"-"*10+"+")


var = 0
print(var==0)
var = 1
print(var==0)


number1 =  int(input("Enter the first number: "))
number2 =  int(input("Enter the second number: "))
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("The larger number is:", larger_number)
'''
####
'''
number1 =  int(input("Enter the first number: "))
number2 =  int(input("Enter the second number: "))
number3 =  int(input("Enter the third number: "))

largest_number = number1
if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3

print("The largest number is:", largest_number)

largest_number = max(number1, number2, number3)
lowest_number = min(number1, number2, number3)
print("The largest number is:", largest_number)
print("The lowest number is:", lowest_number)
'''

##LOOPS


#while True:
#    print("This is an infinite loop")
'''
largest_number = -999999999
number = int(input("Enter a number (or -1 to stop): "))
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number (or -1 to stop): "))
print("The largest number is:", largest_number)
'''
########
# number = int(input("Enter a number: "))
# count = 1
# even =  0
# odd = 0
# while count <= number:
#     if count % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     count += 1
# print("Even=", even)
# print("Odd=", odd)


#########
# for counter in range(100):
#     print("counter:", counter)
#     pass


####
# for counter in range(1, 11, 2):
#     print("counter:", counter)


# ######
# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2

######
# print("The break statement:")
# for counter in range(1, 11):
#     if counter == 5:
#         break
#     print("Inside counter:", counter)
# print("Outside counter")

# print("The break statement:")
# for counter in range(1, 11):
#     if counter == 5:
#         continue
#     print("Inside counter:", counter)
# print("Outside counter")




#Logical Expressions
# var = 10
# print(var>0)
# print(not(var<=0))

# print(var!=0)
# print(not(var==0))



#List
'''
numbers = []
numbers = [1, 2, 3, 4, 5]

print(numbers)
print(type(numbers))
print("first element contents:", numbers[0])
print("second element contents:", numbers[1])
print("third element contents:", numbers[2])
print("fourth element contents:", numbers[3])
print("fifth element contents:", numbers[4])

numbers[0] = 10
print("numbers[0] after modification:", numbers[0])
print(numbers)

numbers[1] = numbers[4]
print(numbers)
print(len(numbers))
del numbers[2]
print(numbers)
print(len(numbers))

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[4]) #IndexError: list index out of range
'''
list = [1, 2, 3, 4, 5]
print(list)
list.append(6)
print(list)

list.insert(0, 0)
print(list)




