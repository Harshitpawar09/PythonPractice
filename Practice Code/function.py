# def message():
#     print("Enter a value: ")
# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())



# def message():
#     print("Enter a value: ")
#     temp = int(input())
#     return temp
# print("Step 1")
# a = message()
# message()
# print("Step 2")
# b = message()
# print("Step 3")
# c = message()
# print("a:", a)
# print("b:", b)
# print("c:", c)



# def message():
#     print("Enter a value: ")
# print("We start here.")
# print(message)
# message()
# print("We end here.")



#arguments and parameters

# def hello(n):
#     print("Hello", n)
# name = input("Enter your name: ")
# hello(name)


# def message(number):
#     print("Enter a number:", number)
# number = 1234
# message(1)
# print(number)


# def message(what, number):
#     print("Enter", what, "number", number)

# message("telephone", 11)
# message("11" , "telephone")
# message("price", 5)
# message("number", "number")  


# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
# introduction("Harshit" , "Buwade")
# introduction("John", "Smith")
# introduction("Jane", "Doe")
# introduction("Alice", "Johnson")

#Keword Arguments Passing
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
# introduction(first_name="Harshit", last_name="Buwade")
# introduction(last_name="Smith", first_name="John")

#Mixing positional and keyword arguments
# def adding(a,b,c):
#     print(a, "+", b, "+", c, "=", a+b+c)
# adding(1,2,3)
# adding(c=1, a=2, b=3)
# adding(1, c=2, b=3)
# # adding(3, a=1, b=2)


# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")
# happy_new_year(True)
# happy_new_year(False)


# def boring_function():
#     print(" 'Boredom Mode' On")
#     return 123
# print("This lesson is interesting.")
# boring_function()
# print("This lesson is boring.")




# def checkMyVar(variable):
#     if (variable == 10):
#         print("Variable is 10")
#         return 2
#     else:
#         print("Varible is not up to the mark")
#         return
# print(checkMyVar(5))




# def list_sum(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#     return sum
# print(list_sum([1, 2, 3, 4, 5]))



# def strange_list_fun(n):
#     strange_list = []
#     for i in range(0, n):
#         # strange_list.insert(0, i+1)
#         strange_list.append(i+1)
#     return strange_list
# print(strange_list_fun(5))




#Scope

# def my_function():
#     x = 123
# my_function()
# print(x) #variable x is not defined outside the function, it will give an error.


# def my_function():
#     print("Do I know the variable ?", var)
# var = 1
# my_function() #variable var is defined outside the function, it will give the value of var as 1.
# print(var)


# def mult(x):
#     var = 7
#     return x * var
# var = 3
# print(mult(7))


def my_function():
    global var
    var = 2
    print("Do I know the variable ?", var)
var = 1
my_function() #variable var is defined as global inside the function, it will change the value of var to 2.
print(var)