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

    def deletebegin(self, key):
        if self.head is None:
            print("empty=LL")
        else:
            print("Deleted node from begining : ",self.head.data)
            self.head=self.head.next

        
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
    print("\n LinkedList - Insert AT End....")
    print("1.Insert")
    print("2.Display")
    print("3.Delete by value")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        data = int(input("Enter a value to insert: "))
        ll.iae(data)
    elif choice == '2':
        ll.display()
    elif choice == '3':
        val = int(input("Enter the value you want to delete: "))
        ll.deletebegin(val)
    elif choice == '4':
        print("Exit the operation")
        break
    else:
        print("Enter only 1 / 2 / 3 / 4")