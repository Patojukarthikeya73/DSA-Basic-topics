def bsearch_range(arr,target,left,right):
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

def expo_search(arr,target):
    if not arr:
        return -1
    if arr[0]==target:
        return 0
    n=len(arr)
    i=1
    while i<n and arr[i]<=target:
        i *=2
    return bsearch_range(arr,target,i//2,min(i,n-1))


arr=[2,4,6,8,10,12,14]
target = 10
result=expo_search(arr,target)
print(f"Element {target} found at index : {result}")