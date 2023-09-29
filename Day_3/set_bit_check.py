#Check wheather the bit of given position is set or not i.e., 1 or not
n=int(input("Enter Number:- "))
k=int(input("Enter bit pos:- "))-1
#method 1:-
if (n>>k)%2==1:
    print("Yes")
else:
    print("No")
#method 2:-
if n&(1<<k):
    print("Yes")
else:
    print("No")