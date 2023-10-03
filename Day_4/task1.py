#Python Bootcamp to revise the basic concepts in python
class A:
    a=1
    b="Anonymous"
    c=3
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def fun1(self,x,y):
        print("Reverse of the input String:- ",x[::-1])
        print("Square of First Variable:- ",y**2)
        #print(y**(1/2))
    def displayResult(self):
        print("Length of the Entered String:- ",len(b))
        print("a%c= ",a%c)
a=int(input("Enter a Number:- "))
b=input("Enter String:- ")
c=int(input("Enter Other Number:- "))
obj=A(a,b,c)
obj.fun1(b,a)
obj.displayResult()