# Given the head of a singly linked list, reverse the list, and return the reversed list.

#-----------------------------------------Brute force--------------------------------------------------------------------

def reverse_list_brute(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    node = head 
    i = len(values) - 1
    while node:
        node.val = values[i]
        node = node.next
        i -= 1
    return head 


#---------------------------------------OPTIMIZED SOLUTION-----------------------------------------------------

def reverse_list(head):
    prev = None                # PREV flag: not placed on anyone yet
    curr = head                # CURR flaf: starts on person at 1 

    while curr:   # keep walking as long as CURR is standing on someone
        next_node = curr.next     # write down on the notepad who CURR is currently holding hands with -- BEFORE we change anything
        curr.next = prev            # CURR lets go, and grabs the hand of whoever PREV is standing on instead (or grabs nothing, if PREV is empty)
        prev = curr          # move the PREV flag forward, onto where CURR is standing (this person is now "flipped")
        curr = next_node     # move the CURR flag forward, onto the name we wrote on the notepad
    return prev          # CURR walked off the end -- PREV is now standing on the new front of the line

"""
Walk through 1 → 2 → 3, three people named 1, 2, 3:

Start: PREV = nobody. CURR = person 1. Notepad = blank.
Loop 1: notepad ← "2" (that's who 1 is currently holding). Person 1 lets go of 2, grabs... nothing (PREV is empty). PREV flag moves to person 1. CURR flag moves to person 2.
Loop 2: notepad ← "3" (who 2 is holding). Person 2 lets go of 3, grabs person 1's hand instead (PREV is standing on 1). PREV flag moves to person 2. CURR flag moves to person 3.
Loop 3: notepad ← nothing (person 3 wasn't holding anyone — end of original line). Person 3 lets go, grabs person 2's hand instead. PREV flag moves to person 3. CURR flag moves to... nothing. Loop stops.
Return: PREV is standing on person 3 — the new front of the line.
"""

