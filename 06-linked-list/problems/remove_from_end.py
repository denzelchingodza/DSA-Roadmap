# Given the head of a linked list, remove the nth node from the end,
# and return the head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy

    # move fast n + 1 steps ahead of slow
    for _ in range(n + 1):
        fast = fast.next

    # move both together until fast runs off the end
    while fast:
        slow = slow.next
        fast = fast.next

    # slow is now right before the node to remove
    slow.next = slow.next.next
    return dummy.next


"""
Trace: [1,2,3,4,5], n = 2 (remove the 2nd node from the end, which is 4)

dummy -> 1 -> 2 -> 3 -> 4 -> 5
Move fast ahead by n+1 = 3 steps from dummy: dummy -> 1 -> 2 -> 3. fast is now on node 3.
Move both together until fast hits None:
slow: dummy->1, fast: 3->4
slow: 1->2, fast: 4->5
slow: 2->3, fast: 5->None -> stop
slow is on node 3, exactly the node before 4. slow.next = slow.next.next skips 4 entirely: 3.next = 5.

Result: 1 -> 2 -> 3 -> 5. Matches.

Why n + 1 and not n: you want slow to land on the node before the target, not on
the target itself -- that extra +1 step is what buys you that one-node offset.
"""
