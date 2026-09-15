# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list by splicing together the existing nodes.
# Return the head of the merged list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#--------------------------BRUTE FORCE---------------------------------------------------------------
def merge_two_lists_brute(list1, list2):
    values = []
    for node in (list1, list2):
        while node:
            values.append(node.val)
            node = node.next
    values.sort()

    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


# --------------------------------OPTIMIZED SOLUTION-----------------------------------------------
def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


"""
Trace: list1 = [1,2,4], list2 = [1,3,4]

step	list1	list2	compare	attach	tail now
1	1	1	1<=1 true	list1's 1	1
2	2	1	2<=1 false	list2's 1	1 -> 1
3	2	3	2<=3 true	list1's 2	1 -> 1 -> 2
4	4	3	4<=3 false	list2's 3	1 -> 1 -> 2 -> 3
5	4	4	4<=4 true	list1's 4	1 -> 1 -> 2 -> 3 -> 4
6	None	4	list1 empty, stop loop	-	-
end	-	-	attach remainder: list2 (just [4])	-	1 -> 1 -> 2 -> 3 -> 4 -> 4

"""
