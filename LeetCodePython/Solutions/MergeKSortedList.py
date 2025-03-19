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

def merge_two_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next

def merge_k_sorted_lists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(merge_two_lists(l1, l2))

        lists = merged_lists

    return lists[0]

# Example usage
ll1 = LinkedList()
ll1.append(1)
ll1.append(4)
ll1.append(7)

ll2 = LinkedList()
ll2.append(2)
ll2.append(5)
ll2.append(8)

ll3 = LinkedList()
ll3.append(3)
ll3.append(6)
ll3.append(9)

lists = [ll1.head, ll2.head, ll3.head]

merged_head = merge_k_sorted_lists(lists)

print("Merged List:")
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.print_list()