#Find the xor of given range inclusively
'''Pattern of first n  numbers
1:1-->1
2:3-->n+1
3:0-->0
4:4-->n
----------------
5:1-->1
6:7-->n+1
7:0-->0
8:8-->n
----------------
9:1-->1
10:11-->n+1
11:0-->0
12:12-->n
....
'''
def xor(n):
    if n%4==0:
        return (n)
    elif n%4==1:
        return (1)
    elif n%4==2:
        return (n+1)
    else:
        return (0)

l=int(input("Enter Initial Number:- "))
r=int(input("Enter Final Number:- "))
#Method 1:-
print(xor(r)^xor(l-1))
#Method 2:-
for i in range(l+1,r+1):
    l^=i
print(l)