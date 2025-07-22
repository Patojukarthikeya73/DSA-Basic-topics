class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def iap (self,data,pos):
        newnode=node(data)
        if pos<=0:
            print("Position min>=1")
            return
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            print(f"{data} inserted at pos-1")
            return
        current=self.head
        c=1
        while current and count < pos-1:
            current=current.next
            c+=1
        if not current:
            print("not in range....")
            return
        newnode.next=current.next
        current.next=newnode
        print("f{data} inserted at position {pos}.")
    
    def display(self):
        current=self.head
        if not current:
            print("LL-empty")
            return 
        while current:
            print(current.data, end='---')
            current=current.next
    print("None")



ll=LinkedList()
while True:
    print("\nLinkedList- Insert At end.....")
    print("1. Insert")
    print("2. Display")
    print("3. search")
    print("4. Exit")
    choice=input("Enter your choice : ")
    if choice=='1':
        data= int(input("Enter a value to insert : "))
        # ll.iap(data)
        pos=int(input("Enter pos:"))
        ll.iap(data,pos)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the opeation...")
        break
    else:
        print("Enter only ...1/2/3")

