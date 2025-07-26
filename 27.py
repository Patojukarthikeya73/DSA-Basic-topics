#At the   end insertion on DLL
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublelinkedlist():
    def __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def display(self):
        temp=self.head
        print("Double  Linked List : ")
        while temp:
            print(temp.data, end="<--")
            temp=temp.next
        print(None)



dll=doublelinkedlist()
n=int(input("Enter a no.of elements to insert at end : "))
for i in range(n):
    value=int(input(f"Enter element {i+1} : "))
    dll.iae(value)
dll.display()