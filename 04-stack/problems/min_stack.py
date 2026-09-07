# design a stack that supports the usual push, pop, top, and a get_min() that returns 
# the minimum element currently in the stack and all four operations need to run in O(1).

class MinStack:
    def __init__(self):
        self.stack = [] #each entry is (value, min_so_far_including_this_value)

    def push(self, val):
        if not self.stack:
            current_min = val #if the stack is empty the current value pushed is the minimum
        else:
            # The new minimum is either the running min so far, or this
            # new value, whichever is smaller
            current_min = min(self.stack[-1][1], val)
        self.stack.append((val, current_min))

    def pop(self):
        self.stack.pop() # removes the (value, min_at_that_time) pair 
        # the min "reverts" automatically, since the new top's stored
        # min reflects the state from before this value was ever pushed.
    def top(self):
        return self.stack[-1][0] # just the value, not the paired min

    def get_min(self):
        return self.stack[-1][1] # the min stored alongside the current top

"""
push(3): stack empty → current_min = 3. stack = [(3, 3)].

push(1): current_min = min(3, 1) = 1. stack = [(3,3), (1,1)].

push(2): current_min = min(1, 2) = 1. stack = [(3,3), (1,1), (2,1)]. get_min() → 1. ✓

pop(): removes (2,1). stack = [(3,3), (1,1)]. get_min() → 1 (from the (1,1) pair, correctly still 1). ✓

pop(): removes (1,1). stack = [(3,3)]. get_min() → 3 — the minimum correctly "reverted" back to 3, automatically, with no recomputation. ✓

"""