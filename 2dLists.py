#2D Lists

#a 2D list is a list where each item in the list is another list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# matrix[0][1]=20 #this will modify the values. instead of 2 it will be 20.
# print(matrix [0][1]) #this will return the 2

#you can use nested loops to iterate over the matrix
for row in matrix:
    for item in row:
        print(item)
        print (item)