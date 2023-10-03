#Find the Rotate the matrix 90 degrees and Mirror of the matrix based on i and j values
matrix=[[1,2,3],[4,5,6],[7,8,9]]
n=3
e=[]
o=[]
for i in range(1,(n**2)+1):
    if i!=5:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
e=e[::-1]
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            matrix[i][j]=((n**2)+1)//2
        elif (i+j)%2==0:
            matrix[i][j]=e.pop()
        else:
            matrix[i][j]=o.pop()
print("Resultant Matrix:- ")
for i in matrix:
    print(i)
print()
print("Rotate Matrix 90 degrees clockwise:- ")
for i in range(n):
    for j in range(n):
        print(matrix[(n-1)-j][i],end=' ')
    print()
print("Mirror Image of the Matrix:- ")
for i in range(n):
    print(matrix[i][::-1])