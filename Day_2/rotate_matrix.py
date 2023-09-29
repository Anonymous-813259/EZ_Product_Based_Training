#Implement a 2d array and rotate the matrix 90 degrees
m,n=int(input("Enter Number of rows: ")),int(input("Enter Number of columns: "))
matrix=[]
print("Enter Matrix row wise: ")
for i in range(n):
    matrix.append(list(map(int,input().split())))
print("Matrix after rotating 90 deg clockwise:- ")
for i in range(m):
    for j in range(n):
        #res_mat.append(matrix[m-1-i][j])
        print(matrix[m-1-i][j],end=' ')
    print()
print("Matrix after rotating 90 deg anti-clockwise:- ")
for i in range(m):
    for j in range(n):
        #res_mat.append(matrix[j][m-1-i])
        print(matrix[j][m-1-i],end=' ')
    print()


#res_mat=[]
"""#transpose the matrix and reverse the columns
#creating a dummy result matrix
for i in range(m):
    temp=[]
    for j in range(n):
        temp.append((matrix[j][i]))
    #appending the col to row and reversing it.
    res_mat.append(temp[::-1])
for i in range(m):
    print(res_mat[i])"""