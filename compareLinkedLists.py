class ListNode:
    def __init__(self, val=''):
        self.val = val
        self.next = None

    def __str__(self):
        node = self
        elements = []
        while node:
            elements.append(node.val)
            node = node.next
        return " -> ".join(elements)   


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def compare_linked_lists(L1: ListNode, L2: ListNode) -> bool:
    L1_ix = L2_ix = 0

    while L1 is not None and L2 is not None: 
        if L1_ix == len(L1.val) or L2_ix == len(L2.val):
            if L1_ix == len(L1.val):
                L1 = L1.next
                L1_ix = 0
            
            if L2_ix == len(L2.val):
                L2 = L2.next
                L2_ix = 0

        elif L1_ix < len(L1.val) or L2_ix < len(L2.val):
            if L1.val[L1_ix] != L2.val[L2_ix]:
                return False
            L1_ix += 1
            L2_ix += 1
    
    if L1 or L2:
        return False

    return True


print(create_linked_list(['hel', '', 'lo']))
print(create_linked_list(['hell', 'o']))

print(compare_linked_lists(create_linked_list(['hel', '', 'lo']),
                           create_linked_list(['hell', 'o'])), True)

print(compare_linked_lists(create_linked_list(['hel', '', 'lo', ' th', 'ere']),
                           create_linked_list(['hell', 'o', '', '', ' ', 'there'])), True)

print(compare_linked_lists(create_linked_list(['hel', '', 'lo']),
                           create_linked_list(['hell', 'o', '3'])), False)

print(compare_linked_lists(create_linked_list(['a']),
                           create_linked_list(['a', '3'])), False)

print(compare_linked_lists(create_linked_list(['']),
                           create_linked_list([''])), True)