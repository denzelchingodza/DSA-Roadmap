# Given the root of a binary tree, return its maximum depth

# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node, down to the farthest leaf node 

def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)

"""
root = [3,9,20,null,null,15,7]

        3
      /   \
     9     20
          /  \
         15   7

max_depth(3) needs answers from both children before it can answer for itself:

max_depth(9): node 9 has no children. left_depth = max_depth(None) = 0, 
right_depth = max_depth(None) = 0. Returns 1 + max(0,0) = 1.
max_depth(20): needs its own two children first.
max_depth(15): no children → returns 1 + max(0,0) = 1.
max_depth(7): no children → returns 1 + max(0,0) = 1.
Back at 20: left_depth = 1, right_depth = 1 → returns 1 + max(1,1) = 2.
Back at the root 3: left_depth = max_depth(9) = 1, right_depth = max_depth(20) = 2 → returns 1 + max(1,2) = 3.
Final answer: 3. Matches — the longest path is 3 → 20 → 15 (or 3 → 20 → 7), 3 nodes deep.

"""