# class ThisIsMyFirstClass:
#     name = "Harshit" #Properties
#     age = 20

#     def getName(self): #Method
#         print(self.name)

# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName()
# print(firstObject.name)

class Student:
    def __init__(self, name, age, gender, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade

    def printDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Grade:", self.grade)

Harsh = Student("Harsh", 21, "Male", "4th year")
print(Harsh)
Harsh.printDetails()

