#Aray operations
#program to consider a list arr=[10,20,30,40]and perform insert operation and deletion operation with 50 and 25 at position 2 respectively and traverse the array to fetch a number 25 is present or not,'''

arr=[10,20,30,40]
#insert
arr.append(50)
arr.insert(2,25)
# print(arr)
for i in arr:
  print(i,end=' ')
#deletion
print("\t")
arr.remove(30)
arr.pop
#print(arr)
#traversal
for i in arr:
  print(i,end=' ')
#searching
print("\n 25 in array?",25 in arr)