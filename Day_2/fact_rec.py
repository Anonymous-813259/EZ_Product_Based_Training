#Factorial of n using recurssion
def fact(n):
    if n<=0:
        return 1
    return n*fact(n-1)
n=int(input("Enter N value:- "))
print(fact(n))