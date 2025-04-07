class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def reverseLinkedlist(head):
        prev=0
        current=head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev    
    # Data Structures Example: Reversing a Linked List
# Problem: Reverse the nodes of a singly linked list.
# Source: ccodelearner.com

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a singly linked list.
    :param head: ListNode, the head of the linked list
    :return: ListNode, the new head of the reversed linked list
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # temporarily store the next node
        current.next = prev       # reverse the current node's pointer
        prev = current            # move pointers one position ahead
        current = next_node
    return prev

def build_linked_list(values):
    """
    Builds a linked list from a list of values.
    :param values: List[int]
    :return: ListNode, the head of the linked list
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """
    Prints the linked list in a readable format.
    :param head: ListNode, the head of the linked list
    """
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))

if __name__ == "__main__":
    # Input: Read space-separated integers for the linked list
    input_str = input("Enter space-separated integers for the linked list: ")
    values = list(map(int, input_str.split()))
    
    # Build the linked list from the input values
    head = build_linked_list(values)
    print("Original Linked List:")
    print_linked_list(head)
    
    # Reverse the linked list
    reversed_head = reverse_linked_list(head)
    print("Reversed Linked List:")
    print_linked_list(reversed_head)
            