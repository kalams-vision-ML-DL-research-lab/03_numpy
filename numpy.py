#03_numpy
import numpy as np
#Array
#1 dim.
ar1 = np.array([2,4,6,8,10])
print("1 dim:",ar1)
print()
print(ar1.dtype)
print(ar1.shape)
print(ar1.ndim)
#2 dim.
print()
ar2 = np.array([[1,3,5,7,9],[0,2,4,6,10]])
print("2 dim:",ar2)
print(ar2.dtype)
print(ar2.shape)
print(ar2.ndim)
#3 dim.
print()
ar3 = np.array([[1,4,9,16],[25,36,49,64],[81,100,121,144]])
print(ar3)
print(ar3.dtype)
print(ar3.shape)
print(ar3.ndim)

#Empty array
em_ar = np.empty((1,4))
print(em_ar)
print(em_ar.ndim)

#array of 1's
ar_1= np.ones((3,3))
print(ar_1)
print(ar_1.ndim)


#3D array
ar_3d = np.array([[[2,3,5,7],[11,13,17,19],[23,29,31,33]],
                 [[37,41,43,47],[59,61,67,71],
                  [73,79,83,85]]
                 ])
print(ar_3d)
print(f"dimensions:,ar_3d.ndim")

#Creat an array in the range.
arng = np.arange(1,10)
print(arng)

#Diagonal array of ones
ar_di = np.eye(3,4)
print(ar_di)

#changing the data type of array
ar1 = np.array([1,22,33,4]) 
print(ar1.dtype)                  
print("Data type: ",ar1.dtype)  

ar2 = np.array([1,22,33,4],
               dtype= np.int8)  #,dtype = np.int8)
print(ar2.dtype)

#change the dimension of the array
ar = np.array([24,45,67],ndmin=2) 

#finding mean, median, SD.
ar = np.array([3,2,4,5,6,7,4,2,2,2,3,3,6,7,8,1]) 
print(np.mean(ar)) 
print() 
print(np.sort(ar))
print() 
print(np.median(ar)) 
