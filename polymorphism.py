# class One:
#     def do_it(self):
#         print("do_it from One")
#     def doanything(self):
#         self.do_it()
# class Two(One):
#     def do_it(self):
#         print("do_it from Two")
# one = One()
# two = Two()
# one.doanything()
# two.doanything()



#Exception handling

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("This is always executed")
#     return n
# print("reciprocal(2):", reciprocal(2))
# print("reciprocal(0):", reciprocal(0))





# try:
#     i = int("Hello")
# except Exception as e:
#     print(e)
#     print(e.__str__())




class MyZeroDivisionError(ZeroDivisionError):
    pass
def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")
do_the_division(False)