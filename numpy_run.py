import numpy as np

# # Create Arrays
# arr1d = np.array([1, 2, 3, 4, 5])
# arr2d = np.array([[34, 65, 24], [53, 87, 50], [29, 36, 95]])

# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.ndim)



# zeros = np.zeros((3,4))
# print(zeros)
# ones = np.ones((2,5))
# print(ones)
# rng = np.arange(0,50,5)
# print(rng)
# lin = np.linspace(0,1,11)
# print(lin)
# random = np.random.randint(40,100,(5,3))
# print(random)



# arr = np.array([10,20,30,40,50])
# print(arr * 2)
# print(arr + 5)
# print(arr ** 2)




#Statics Operation
# marks_2d = np.array([[85,90,78], [72,88,95], [91,76,83]])
# print(np.mean(marks_2d))
# print(np.mean(marks_2d, axis=1))
# print(np.mean(marks_2d, axis=0))
# print(np.max(marks_2d))
# print(np.std(marks_2d))




arr = np.array ([55,82,43,91,67,78,35,88])
print(arr[arr > 70])