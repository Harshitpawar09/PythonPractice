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


# class Classy:
#     def method(self, par):
#         print("method", par)
# obj = Classy()
# obj.method(1)


# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)
# obj = Classy()
# obj.var = 3
# obj.method()


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
# sun = Star("Sun", "Milky Way")
# print(sun)


#str method


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     def __str__(self):
#         return self.name + ' in ' + self.galaxy
# sun = Star("Sun", "Milky Way")
# print(sun)



# class Vehicle:
#     pass

# class LandVehicle (Vehicle):
#     pass
    
# class TrackedVehicle (LandVehicle):
#     pass
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print (issubclass(cls1, cls2),end="\t")
#     print()


# class Super:
#     supVar = 1
# class Sub(Super) :
#     subVar = 2
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


# class Super:
#     def __init__(self):
#         self.supVar = 11

# class Sub (Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


#MultiLevel Inheritance

'''
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1 (self):
        return 102
    
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2 (self):
        return 202
    
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302
    
obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
'''




#Class Varaible

# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         self.__first = val
#         ExampleClass.counter += 1

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)   


# #Try Except Block
# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
# example_object = ExampleClass(2)
# try:
#     print("a = ", example_object.a)
# except AttributeError:
#     try:
#         print("b = ", example_object.b)
#     except AttributeError:
#         print("The error occurred ! Silently passing it !!")




# class ExampleClass:
#     counter = 0
#     a = 1
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
# example_object = ExampleClass(1)
# if hasattr(example_object, 'a'):
#     print("a = ", example_object.a)
# if hasattr(example_object, 'b'):
#     print("b = ", example_object.b)
# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))






# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 1
#         self.__venomous = False
# myObj = Python()
# print("myObj.population:", myObj.population)
# print("myObj.victims:", myObj.victims)
# print("myObj.length_ft:", myObj.length_ft)
# print("myObj.__venomous:", myObj._Python__venomous)
# # print("myObj.venomous:", myObj.venomous)



#Name Mangling in methods
class Classy:
    def visible(self):
        print("This is a visible method")
    def __hidden(self):
        print("This is a hidden method")
obj = Classy()
obj.visible()
try:
    obj.__hidden()
except:
    print("Failed")
obj._Classy__hidden()