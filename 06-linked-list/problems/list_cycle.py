# Given head, determine if the linked list has a cycle in it (some node's next 
# eventually loops back to a node earlier in the list, instead of ending in None).

# ---------------------------------------BRUTE FORCE-----------------------------------------------
def has_cycle_brute(head):
    seen = set()
    node = head
    while node:
        if node in seen:
            return True
        seen.add(node)
        node = node.next
    return False 
# O(n) time, O(n) space, you are basically storing every node just to check "have i seen this before"

# ---------------------------------OPTIMIZED SOLUTION-----------------------------------------------------

#Floyd's fast and slow pointers (tortoise and hare)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True 
    return False 
# O(n) time, O(1) space complexity

"""
Trace: 1 -> 2 -> 3 -> 4, where 4's .next points back to 2 (a cycle).
step	slow	fast
start	1	1
1	2	3
2	3	2 (fast: 3→4→2)
3	4	4 (fast: 2→3→4) → slow == fast → return True

Notice fast looped back into the cycle and caught up to slow from behind 
that collision is the whole detection mechanism.

Why while fast and fast.next and not just while fast: fast moves two steps 
per loop (fast.next.next). If fast.next were None, trying to read .next.next 
would crash. Checking both keeps you from stepping off the edge.
"""