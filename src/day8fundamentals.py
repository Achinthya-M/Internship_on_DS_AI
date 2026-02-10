# -*- coding: utf-8 -*-
import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6]])
b = np.array([10, 20, 30])
c = np.array([[20,30,40],[10,30,50],[70,80,90]])
d = np.array([])
print("1d array:",b)
print("2d array:",a)
print("3d array:",c)
print("0 array:",d)
result = a + b
print(result)
# Vectorized vs Loop example
arr = np.random.rand(1000000)
# Vectorized
squared = arr ** 2
print(squared)

arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])
vstacked = np.vstack((a, b))
print(vstacked)
hstacked = np.hstack((a,b))
print(hstacked)

data = np.array([[10, 20, 30],
                 [40, 50, 60]])
print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data, axis=1))

A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
print(np.dot(A, B))

arr = np.linspace(0,4,5)
print(arr)

arr = np.random.rand(2,2)
print(arr)

arr = np.random.randn(2,3)
print(arr)

arr = np.random.uniform(20,30,size=(2,2))
print(arr)
print(arr.dtype)

arr = np.array([1.2,2.8,-3.7])
print(np.floor(arr))

arr = np.array([1.2,2.8,-3.7])
print(np.ceil(arr))#nearest value
print("trunc",np.trunc(arr))#removes decimal points
print("round",np.round(arr))

#task 1
scores = np.random.randint(50, 101, size=(5, 3))
subject_mean = scores.mean(axis=0)
centered_scores = scores - subject_mean
print("Original Scores:\n", scores)
print("Subject-wise Mean:\n", subject_mean)
print("Centered Scores:\n", centered_scores)

#task 2
data=np.arange(24)
reshaped=data.reshape(4,3,2)
transposed=reshaped.transpose(1,0,2)
print("Final shape:\n",transposed.shape)
print("Final array:\n",transposed)