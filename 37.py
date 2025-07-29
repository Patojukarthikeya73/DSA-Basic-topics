#Code check thhe duplicates in a DLL and print the count  of frequency
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        dll_str = ""
        while curr:
            dll_str += str(curr.data)
            if curr.next:
                dll_str += "<-->"
            curr = curr.next
        print("\nDLL")
        print(dll_str)

    def find_duplicates(self):
        freq = {}
        curr = self.head
        while curr:
            freq[curr.data] = freq.get(curr.data, 0) + 1
            curr = curr.next
        print("\nduplicate values in DLL:")
        for val, count in freq.items():
            if count > 1:
                print(f"{val} appears {count} times")

dll = DoublyLinkedList()
n = int(input("Enter the number of elements: "))
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    dll.append(val)

dll.display()
dll.find_duplicates()
