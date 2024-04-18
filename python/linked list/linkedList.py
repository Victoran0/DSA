 class Node:
    def __init__(self, a_number):
        self.data = a_number
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


def reverse(l):
    if l.head is None:
        return

    current_node = l.head
    prev_node = None

    while current_node is not None:
        # track the next node
        next_node = current_node.next

        # modify the current node
        current_node.next = prev_node

        # update prev and current node
        prev_node = current_node
        current_node = next_node

    l.head = prev_node

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

reverse(list2)

print(list2.show_elements())


# QUESTION: You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     ls1 = []
#     while list1:
#         ls1.append(list1.val)
#         list1 = list1.next
#     ls2 = []
#     while list2:
#         ls2.append(list2.val)
#         list2 = list2.next
#     ls = ls1 + ls2
#     ls.sort()
#     s = t = ListNode()
#     for i in ls:
#         s.next = ListNode(i)
#         s = s.next
#     return t.next











