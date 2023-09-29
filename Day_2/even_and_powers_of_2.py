#Create the 1-d array, it should contain numbers between the given range(no double elements), extract and print the following:-
#1. Even numbers
#2. Powers of 2
limit1=int(input("Enter lower Limit:- "))
limit2=int(input("Enter upper Limit:- "))
size=int(input("Enter Array Size:- "))
l=list(map(int,input("Enter List Elements:- ").split()))
if size<=(limit2-limit1)+1:
    print(f"Even Number between {limit1} and {limit2} from the given list:- ",end=' ')
    for i in l:
        if i>=limit1 and i<=limit2 and i%2==0:
            print(i,end=' ')
    print()
    print(f"Powers of 2 between {limit1} and {limit2} from the given list:- ",end=' ')
    for i in l:
        if i>=limit1 and i<=limit2:
            j=1
            while(2**j<=i):
                if i==2**j:
                    print(i,end=' ')
                j+=1
    """d={
        2 : 1,
        4 : 2,
        8 : 3,
        16 : 4,
        32 : 5,
        64 : 6,
        128 : 7,
        256 : 8,
        512 : 9
    }
    print(f"Powers of 2 between {limit1} and {limit2} from the given list:- ",end=' ')
    for i in l:
        if i>=limit1 and i<=limit2 and i in d:
            print(i,end=' ')"""
