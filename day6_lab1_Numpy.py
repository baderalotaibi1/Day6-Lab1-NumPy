import numpy as np
x=np.ones(3)
y=np.zeros(3)
a=x+y
print("Q#3: Add x and y arrays.\n",a)
print("Q#4: Print x array characteristics (e.g: dimension, shape, size, type)\n",x.shape,x.ndim,x.size,x.dtype)
w=np.array([[11,12],
            [13,14],
            [15,16]])
print("Q#5: Create a 2D array called w as the following: \n",w)
z=np.arange(1,3)
print("Q#6: Create z array contains the numbers from 1 to 3.\n",z)
newArray=np.row_stack((z,w))
print("Q#7: Combine the arrays z and w in vertical way then save it in a new variable newArray\n",newArray)
for item in newArray.flat:
    print("Q#8: Print all elements of newArray using the loop.\n",item)
newArray=np.flip(newArray)
print("Q#9: Reverse the columns and rows of newArray.\n",newArray)
newArray-=1
print("Q#10: Decrement all elements of newArray with 1.\n",newArray)
print("Q#11: Find smallest and biggest values in newArray.\n",newArray.min(),newArray.max())
print("Q#12: Print the first row of newArray using indexing.\n",newArray[0])
print("Q#13: Print the number equals 12 of newArray using indexing.\n",newArray[1,1])
print("Q#14: Print the numbers equal 0 and 13 of newArray using Slicing.\n",newArray[1,0],newArray[3,1])
newArray=newArray.reshape(9,1)
print("Q#15: Change the shape of newArray to (9,1).\n","Error: cannot reshape array of size 8 into shape (9,1)")
newArray=newArray.reshape(3,2)
print("Q#16: Change the shape of newArray to (3,2).\n","Error: cannot reshape array of size 8 into shape (3,2)")
