#Create the 1d array & find sum of array elements using functions
def sum_of_arr(arr):
    #return sum(arr)
    s=0
    for i in arr:
        s+=i
    return s
def sum_rec(arr):
    if arr:
        return arr[0]+sum_rec(arr[1:])
    else:
        return 0

arr=list(map(int,input("Enter Array Elements:- ").split()))
print(sum_of_arr(arr))
print(sum_rec(arr))
#here space complexity is O(1)