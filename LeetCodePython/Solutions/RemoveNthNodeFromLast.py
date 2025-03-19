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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    def reverse_list(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def remove_nth_from_end(self, n):
        self.head = self.reverse_list(self.head)
        
        if n == 1:
            new_head = self.head.next
            self.head = self.reverse_list(new_head)
            return
        
        current = self.head
        prev = None
        for _ in range(n - 1):
            prev = current
            current = current.next
        
        if prev is not None and current is not None:
            prev.next = current.next
        
        self.head = self.reverse_list(self.head)

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original List:")
ll.print_list()

n = 2
ll.remove_nth_from_end(n)

print(f"List after removing {n}th node from the end:")
ll.print_list()