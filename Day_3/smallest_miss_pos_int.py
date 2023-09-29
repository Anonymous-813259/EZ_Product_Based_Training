#Find the smallest positive integer missing in the given array starting from 0
#time complexity is O(n^2) and Space complexity is O(1)
a=list(map(int,input("Enter Elements:- ").split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
i,flag=0,0
while(a[i]<0):
    a=a[1:]
for i in range(len(a)):
    if i!=a[i]:
        print(i)
        flag=1
        break
if flag==0:
    print(a[-1]+1)
#time complexity is O(n) and Space complexity is O(n)
d=dict()
a=list(map(int,input("Enter Elements:- ").split()))
for i in a:
    if i>=0 and i not in d:
        d[i]=1
for i in range(len(a)):
    if i not in d:
        print(i)
        flag=1
        break
mx=-1
for i in a:
    if mx<i:
        mx=i
if flag==0:
    print(mx+1)