def linear_search(arr,num):
    if not arr:
        return "No Element"
    elif num==arr[0]:
        return num
    elif arr:
        return linear_search(arr[1:],num)
arr=list(map(int,input("Enter Elements:- ").split()))
num=int(input("Enter Number to find:- "))
print(linear_search(arr,num))