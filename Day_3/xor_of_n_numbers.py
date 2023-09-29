#Find the xor of first n numbers.
n=int(input("Enter Number:- "))
#method 1:-
res=n
for i in range(n):
    res^=i
print(res)
#method 2:- (Analysis Patterns)
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
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
else:
    print(0)