#All numbers in array are repeated exactly twice, except one. Find that one number.
a=list(map(int,input("Enter Elements:- ").split()))
res=0
for i in a:
    res=res^i
print(res)

