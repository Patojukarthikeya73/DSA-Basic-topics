def csort(arr):
    if not arr:
        return []
max_val = max(arr)
count=[0]*(max_val+1)

#freq
for num in arr:
    count[num]+=1
#count
for i in range(1, len(count)):
    count[i]+=count[i-1]
output = [0] * len(arr)

for num in reversed(1, len(count)):
    count[i]+=count[i-1]
output= [0] * len(arr)

#stable sort
for num in reversed(arr):
    output[count[num]-1]=num
    count[num]-=1
#coping sorted list
for i in range(len(arr)):
    arr[i]=output[i]
arr=[4,2,2,8,3,3,1]
print("before", arr)
csort(arr)
print("After :",arr)