#Swaping of given two numbers using xor operators.
a=int(input("Enter a value:- "))#24
b=int(input("Enter b value:- "))#9
print(f"Before Swaping\na={a}\nb={b}")
a=a^b#a=24^9
b=a^b#b=(24^9)^9=24
a=a^b#a=(24^9)^24=9
print(f"After Swaping\na={a}\nb={b}")