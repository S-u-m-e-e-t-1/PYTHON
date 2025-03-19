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

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    return dummy.next

# Example usage
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("List 1:")
ll1.print_list()

print("List 2:")
ll2.print_list()

merged_head = merge_sorted_lists(ll1.head, ll2.head)

print("Merged List:")
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()