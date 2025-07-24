class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iae(self, data):  
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            print(f"{data} inserted at end /will be first node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        print(f"{data} inserted last")

    # def delete_begin(self):
    #     if self.head is None:
    #         print("Empty-LL")
    #     else:
    #         print("Deleted node from beginning:", self.head.data)
    #         self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Empty-LL")
            return
        if self.head.next is None:
            print(f"Deleted last node:{self.head.data}")
            self.head=None
            return
        current=self.head
        while current.next.next:
            current=current.next
        print(f"Deleted last node:{current.next.data}")
        current.next=None
    def display(self):
        current = self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data, end='---')
            current = current.next
        print()

ll = LinkedList()
while True:
   
    print("1. Insert")
    print("2. Display")
    # print("3. Delete by value")
    print("3. Delete at end")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter a value to insert: "))
        ll.iae(data)
    elif choice == '2':
        ll.display()
    # elif choice == '3':
    #     key = int(input("Enter the value you want to delete: "))
    #     ll.delete_by_value(key)
    #     ll.display()
    elif choice == "3":
        ll.delete_end()
        ll.display()
    elif choice == '4':
        print("Exit")