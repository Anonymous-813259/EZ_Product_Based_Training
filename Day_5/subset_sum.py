"""Find the subset of a matrix such that those elements sum is equal to target sum:- 
3 cases:-
1) If last number < target, then consider the last number
2) If last number < target, then don't consider the last number
3) If last number > target, then Ignore that number
"""
#In the below code the arr will be created again with a new address and with the decreased elements
def subset_sum(arr,target):
    if target==0:
        return True
    if not arr:
        return False
    val1=False
    val2=False
    if arr[-1]<=target:
        val1 = subset_sum(arr[:-1],target-arr[-1])#Considered the last element
        val2 = subset_sum(arr[:-1],target)#Not considered the last element
    else:
        val1 = subset_sum(arr[:-1],target)#Ignoring the last element
    return val1|val2
l=list(map(int,input().split()))
target=int(input())
print(subset_sum(l,target))

#Sir code:-
"""#Below code is passed with the same arr location. It won't create any new location for that arr
def subset_sum(arr,n,target):
    #print(target)
    print(id(arr))
    if target==0:
        return True
    if n<0:
        return False
    val1=False
    val2=False
    '''if arr[n]<=target:
        return subset_sum(arr,n-1,target-arr[n]) or subset_sum(arr,n-1,target)
        #val1 = subset_sum(arr,n-1,target-arr[n])#Considered the last element
        #val2 = subset_sum(arr,n-1,target)#Not considered the last element
    else:
        return subset_sum(arr,n-1,target)
        #val1 = subset_sum(arr,n-1,target)#Ignoring the last element
    #return val1|val2'''
    if arr[n]>target:
        return subset_sum(arr,n-1,target)
    return subset_sum(arr,n-1,target-arr[n]) or subset_sum(arr,n-1,target)
l=list(map(int,input().split()))
target=int(input())
print(subset_sum(l,len(l)-1,target))"""