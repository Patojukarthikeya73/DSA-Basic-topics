#Backtraversing
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
        if self.head is None:
            self.head=newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp
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
dll.backtraverse()