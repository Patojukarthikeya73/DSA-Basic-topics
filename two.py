def linear_search(arr,key):
    for i in range(len(arr)):

        if arr[i]==key:
            return i
    return -1


size=int(input("Enter the size of array :"))
arr=[]
print("Enter the elements")
for i in range(size):
    num=int(input(f"Element {i+1} :"))
    arr.append(num)
key=int(input("Enter the element to search :"))
result = linear_search(arr,key)
if result != -1:
    print(f"\n Element {key} found at {result}")
else:
    print(f"\n Element {key} not found" )