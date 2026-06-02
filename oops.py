# class ThisIsMyFirstClass:
#     name = "Harshit" #Properties
#     age = 20

#     def getName(self): #Method
#         print(self.name)

# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName()
# print(firstObject.name)

# class Student:
#     def __init__(self, name, age, gender, grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade

#     def printDetails(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Gender:", self.gender)
#         print("Grade:", self.grade)

# Harsh = Student("Harsh", 21, "Male", "4th year")
# print(Harsh)
# Harsh.printDetails()

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val

#     def set_second(self, val):
#         self.second = val

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1)
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)


class Classy:
    def method(self, par):
        print("method", par)
obj = Classy()
obj.method(1)