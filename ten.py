# Bubble sort
# pseudo code:
# for i->0 to n-1:
# for j->0 to n-i-2:
# if a[j]>a[j+1]
# swap(a[j],a[j+1])
# Code:
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-2):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
size=int(input("Enter the no.of Elements :"))
arr=[]
print("Enter the elements: ")
for i in range(size):
    arr.append(int(input()))
print("Original list :", arr)
bubble_sort(arr)
print("BubbleSorted arr:", arr) 