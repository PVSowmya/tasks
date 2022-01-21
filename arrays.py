import numpy as np
import tkinter
#creating array as list 
arr = np.array([1, 2, 3, 4, 5])

#creating array as tuple
ar=np.array((1,2,3))

#1D,2D,3D arrays
a=np.array(45)
print(a)
print(a.ndim)

b=np.array((1,2,4))
print(b)
print(b.ndim)

c=np.array(((1,2,4),(4,3,8)))
print(c)
print(c.ndim)

d=np.array([[(1,2,4),(4,3,8),(6,3,8)],[(1,2,4),(4,3,8),(6,3,8)]])
print(d)
print(d.ndim)


#asarray
tup=([1, 3, 9], [8, 2, 6])
res=np.asarray(tup)
print(res)

#nditer
for x in np.nditer(res):
    print(x)

#frombuffer
line=b"hello everyone"
res1=np.frombuffer(line,dtype="S1")
print(res1)

#arange
arr1=np.arange(1,10,dtype=float)
print(arr1)

#linspace
res2=np.linspace(20, 40, num=5, endpoint=False,retstep=True,dtype=int)
print(res2)

#logspace
res3=np.logspace(2,3, num=5,dtype=int)
print(res3)

#randint
arr2=np.random.randint(1,100,6)
print(arr2)

#rand()
arr4=np.random.rand(9)
print(arr4)

#shape
my_arr=[[[1,2],[1,7],[6,9]]]
my_res=np.shape(my_arr)
print(my_res)

#reshape
my_res1=np.reshape(my_arr,(3,2))
print(my_res1)

#ones
arr1=np.ones((2,3),dtype=int)
print(arr1)

#zeros
arr2=np.zeros(3)
print(arr2)

#full-initilizes with a value given by user
print(np.full((2,3),10))

#eye-only diagnol elements as 1 and remaining as 0
print(np.eye(3))

#accessing elements of 1D array
one=np.array([1,2,4,56,7,8,98])
print(one[5])
print(one[-3])
print(one[0:5:2])

#accessing elements of 2D array and slicing
two=np.array([[1,7,3],[9,4,5],[3,1,6]])
print(two[1,2])
print(two[0,0:2])
print(two[0:2,0:2])

#axis 0-col,1-rowwise
print(np.sort(two,axis=0))
print(np.sort(two,axis=1))

#accessing elements of 3D array and slicing
three=np.array([[[1,2,3],[3,4,5]],[[3,8,6],[7,9,5]]])
print(three[1,1,1])
print(three[0,0,0:2])

#copy and view
ex = np.array([1, 2, 3, 4, 5])
x = ex.copy()
ex[0]=42

print(ex)
print(x)

#view
av= np.array([1, 2, 3, 4, 5])
y = av.view()
av[0] = 42

print(av)
print(y)

#base of copy and view-copies owns the data, and views does not own the data
ab = np.array([1, 2, 3, 4, 5])

x1 = ab.copy()
y1= ab.view()
print(x1.base)
print(y1.base)

#concatenate
arr1=np.arange(6).reshape(2,3)
arr2=np.arange(7,13).reshape(2,3)
print(np.concatenate((arr1,arr2),axis=1))

#stack()
print(np.stack((arr1,arr2)))
print(np.stack((arr1,arr2),axis=1))

#vstack
print(np.vstack((arr1,arr2)))

#hstack
print(np.hstack((arr1,arr2)))

#dstack
print(np.dstack((arr1,arr2)))

#split,if unequal divisions array_split
sp=np.array([1,2,3,4,7,4,9,6])
print(np.split(sp,4))
print(np.array_split(sp,3))

#Statistical functions
#min and max
sf=np.array([[12,5,7],[4,9,1],[4,8,2]])
print(sf)
print(np.amax(sf))
print(np.amax(sf,axis=0))
print(np.amax(sf,axis=1))
print(np.amin(sf))
print(np.amin(sf,axis=0))
print(np.amin(sf,axis=1))

#average
print(np.average(sf))
#weighted average
w=[1,2,3]
print(np.average(sf,weights=w,axis=0))

#mean
print(np.mean(sf))
print(np.mean(sf,axis=0))

#median
print(np.median(sf))
print(np.median(sf,axis=0))
print(np.median(sf,axis=1))

#variance and standard deviation
print(np.var(sf))
print(np.std(sf))

#sort
print(np.sort(sf,axis=0))

d = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Ajay', 1.8, 41), ('vijay', 1.9, 38), ('sanjay', 1.7, 38)]
k= np.array(values,dtype=d)      
print(np.sort(k, order='height'))

#arithmetic
a1=np.array([[1,2,3],[2,8,5],[6,8,4]])
a2=np.array([[1,8,5],[5,7,2],[6,3,9]])
print(np.add(a1,a2))
print(np.subtract(a1,a2))
print(np.multiply(a1,a2))
print(np.divide(a1,a2))
print(np.mod(a1,a2))
print(np.power(a1,a2))
print(np.reciprocal(a1))
print(np.mod(a1,10))











