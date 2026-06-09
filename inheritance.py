#isinstance

# class Vehicle:
#     pass
# class LandVehicle (Vehicle):
#     pass
# class TrackedVehicle (LandVehicle):
#     pass
# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()
# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print (isinstance(obj, cls),end="\t")
#     print()



# class SampleClass:
#     def __init__(self, val):
#         self.val = val
# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1
# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary had a little"
# string_2 = "Mary had a little lamb"
# string_1 += " lamb"
# print(string_1 == string_2, string_1 is string_2)





# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "My name is " + self.name + "."
# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)
# obj = Sub("John")
# print(obj)





#Multiple Inheritance

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11

# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21

# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())


# Multilevel Inheritance
# class Level1:
#     var = 100
#     def fun(self):
#         return 101
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
# class Level3(Level2):
#     pass
# obj = Level3()
# print(obj.var, obj.fun())




#Multiple inheritance 

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"
class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"
class Sub(Left, Right):
    pass
obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())