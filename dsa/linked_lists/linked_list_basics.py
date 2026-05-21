# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 2. Print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Find length
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # 4. Search for an element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # 5. Delete a node
    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next

    # 6. Reverse a linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 7. Detect cycle in linked list
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 8. Find middle of linked list
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

# Testing
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.print_list()               # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
print(ll.length())            # Output: 5
print(ll.search(3))           # Output: True
ll.delete(3)
ll.print_list()               # Output: 1 -> 2 -> 4 -> 5 -> None

ll2 = LinkedList()
ll2.insert(1)
ll2.insert(2)
ll2.insert(3)
ll2.insert(4)
ll2.insert(5)

ll2.reverse()
ll2.print_list()              # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
print(ll2.has_cycle())        # Output: False
print(ll2.find_middle())      # Output: 3