class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 🚀 Execution Starts Here
ll = LinkedList()

n = int(input("Enter number of nodes: "))
for i in range(n):
    val = input(f"Enter value for node {i+1}: ")
    ll.append(val)

print("\n🔗 Linked List:")
ll.display()

middle = ll.find_middle()
print(f"\n🎯 Middle value: {middle}")
