#Sum of n numbers using recurssion
def sum_of_n_numbers(n):
    if n<=0:
        return 0
    return n+sum_of_n_numbers(n-1)
n=int(input("Enter N Values:- "))
print(sum_of_n_numbers(n))
