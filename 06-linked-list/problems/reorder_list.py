# Given the head of a singly linked list, reorder it into the pattern 
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ... first node, then last node, 
# then second node, then second-to-last, alternating inward. You must do 
# this by rewiring existing nodes, not by changing any .val.

#----------------------------Brute force-------------------------------------------------
def reorder_list_brute(head):
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next

    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j:
            break
        nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None

# Time O(n), space O(n)

# -------------------------OPTIMIZED SOLUTION-----------------------------------------------------------
"""
solved in 3 steps:
1. find the middle with fast slow pointers
2. reverse the second half in place
3. merge the two halves alternately, first-half node, then second-half node, 
repeat, splicing .next pointers as you weave them together.
"""
def reorder_list(head):
    if not head or not head.next:
        return 

    # find the middle 
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    #slow is now sitting on the middle node 

    # reverse the second half, starting right after the middle 
    second = slow.next 
    slow.next = None
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second 
        second = next_node 
    second = prev 

    # weave first half and (reversed) second half together
    first = head 
    while second:
        tmp1, tmp2 = first.next, second.next 
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

"""
Trace: [1,2,3,4,5]

Step 1 — find middle: slow/fast walk: slow ends at node 3 (fast ran off the end 
after 2 hops: 1→3→5, 1→2→3→4→5... fast hits None after landing past 5). Middle = 3.

Step 2 — reverse second half: cut after 3, so first half is 1→2→3, second half 
is 4→5. Reversing 4→5 gives 5→4.

Step 3 — weave: first = 1→2→3, second = 5→4.

first=1, second=5: 1.next = 5, 5.next = 2 (the old first.next), move on → first=2, second=4
first=2, second=4: 2.next = 4, 4.next = 3 (old first.next), move on → first=3, second=None
second is now None, loop stops.

Result: 1 → 5 → 2 → 4 → 3. Matches the expected output.
"""

