#Selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
size=int(input("enter the no.of elements :"))
arr=[]
print("Enter ",size,"elements")
for _ in range(size):
    num=int(input())
    arr.append(num)
result= selection_sort(arr)
print("Sorted array :", result)
