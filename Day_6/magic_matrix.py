#Program to create the magic matrix
n=int(input("Enter the order of the matrix:- "))
mat=[]
for i in range(n):
    l=[]
    for j in range(n):
        l.append(-1)
    mat.append(l)
i=0
j=n//2
num=1
while num<=n**2:
    if i==-1 and j==n:
        i+=2
        j-=1
    elif i==-1:
        i=n-1
    elif j==n:
        j=0
    elif mat[i][j]!=-1:
        i+=2
        j-=1
    mat[i][j]=num
    num+=1
    i-=1
    j+=1
for i in mat:
    print(i)