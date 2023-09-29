#Printing fibonacci series using recurssion
def fib(a,b,n):
    if n<=0:
        return
    print(a+b,end=' ')
    fib(b,a+b,n-1)
n=int(input("Enter N value:- "))
if n==1:
    print("0",end=' ')
elif n>=2:
    print("0 1",end=' ')
#print("0 1",end=' ')
fib(0,1,n-2)