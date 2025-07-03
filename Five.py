import math
def jump_search(arr,target):
    if not arr:
        return -1
    n=len(arr)
    step=int(math.sqrt(n))
    prev=0
    while prev<n and arr[prev]<target:
        prev+=step
    for i in range(max(0,prev-step),min(n,prev+1)):
        if arr[i]==target:
            return i
    return -1

import math
arr=[1,2,3,4,5,6,7]
target =5
result=jump_search(arr,target)
print(f"Element {target} found at index : {result}")
