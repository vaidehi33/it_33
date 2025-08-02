import numpy as np
print(np.__version__)
a=np.array([2,6,1,9,10,3,27])
print(a)

print("---------------------------------")

arr = np.array([[11, 12, 13],
                [4, 5, 6],
                [10, 8, 9]])
arr[:, [0, 1]] = arr[:, [1, 0]]
print(arr)

print("---------------------------------")
a = np.array([2, 6, 1, 9, 10, 3, 27])
result = np.where((a > 5) & (a < 20), a, 0)
filtered = a[(a > 5) & (a < 20)]
print((filtered,))
print("---------------------------------")

a = np.arange(10)
print(a)
print("---------------------------------")
arr = np.full((3, 3), True)
print(arr)

print("---------------------------------")

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_numbers = arr[arr % 2 == 1]
print(odd_numbers)
print("---------------------------------")

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1

print(arr)

print("---------------------------------")


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

out = np.where(arr % 2 == 1, -1, arr)

print("out")
print(out)

print("arr")
print(arr)

print("---------------------------------")

arr = np.arange(10)
out = arr.reshape(2, 5)
print(out)

print("---------------------------------")

a = np.array([2, 6, 1, 9, 10, 3, 27])
out = a[(a >= 5) & (a <= 10)]
print((out,))



