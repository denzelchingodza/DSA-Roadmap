# Given a string of (){}[] characters, determine if the brackets are properly closed and nested 
# every opening bracket has a matching closing bracket of the same type, in the correct order.

def is_valid(s):
    # map each closing bracket to the opening it should match
    pairs = {')':'(', 
             ']':'[',
             '}':'{'}
    stack = []

    for ch in s:
        if ch in pairs:
            # ch is a CLOSING bracket step 3's check.
            # If the stack is empty, there's nothing to close invalid.
            # If the top of the stack doesn't match, wrong bracket type invalid
            if not stack or stack[-1] != pairs[ch]:
                return False 
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

"""
s = "([)]"
( → opening, push. stack = ['(']

[ → opening, push. stack = ['(', '[']

) → closing. Top of stack is '[', but pairs[')'] = '(' — mismatch ('[' != '(') → return False immediately. Correctly invalid, without ever needing to look further.

Compare with s = "()[]{}": every closing bracket matches the top the instant it appears, stack ends empty → True.

The leap: the naive instinct might be counting brackets ("3 opens, 3 closes, 
must be balanced") — but that misses order entirely ("([)]" has 2 opens and 
2 closes of each type and would pass a count-only check, yet it's invalid). 
A stack is what makes "order," specifically "most-recent-first," checkable at all.

"""