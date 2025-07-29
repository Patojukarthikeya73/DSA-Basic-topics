#Insert at end and Delete at end
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinnkedList:
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp

    def dae(self):
        if not self.head:
            print("Cant perform delete in an empty list....")
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        print(f"Deleted: {temp.data}")
        if temp.prev:
            temp.prev.next=None
        else:
            self.head=None


    
    def backtraverse(self):
        print("values for traversig backward........")
        temp=self.head
        if not temp:
            print("Empty list")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end='<---->')
            temp=temp.prev
        print("None")
    def display(self):
        temp=self.head
        print("Doubly Linked List: ")
        while temp:
            print(temp.data, end="<->")
            temp=temp.next
        print("None") 
dll=DoublyLinnkedList()
n=int(input("Enter the no.of elements to insert at end: "))
for i in range(n):
    val=int(input(f"Enter element {i+1} : "))
    dll.iae(val)
dll.display()
d=int(input("\n How many times you want to perform del op: "))
for _ in  range(d):
    dll.dae()
dll.backtraverse()