# Given the root of a binary tree, invert the tree, and return its root

def invert_tree(root):
    if not root:
        return None # base case: nothing here, nothing to mirror 

    left_inverted = invert_tree(root.left) #fully mirror everything under the left side first
    right_inverted = invert_tree(root.right)  #fully mirror everything under the right side first

    root.left = right_inverted
    root.right = left_inverted

    return root 

# ------------------------------OR----------------------------------------------------------------------
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# For time complexity both touch every node eactly once. O(n) either brute or not
# it does differ however on space. 

"""
Full trace 
root = [4,2,7,1,3,6,9]:

        4
      /   \
     2     7
    / \   / \
   1   3 6   9

invert_tree(4) needs invert_tree(2) and invert_tree(7) to finish before it can do anything 
so we go all the way down first:

invert_tree(2) needs invert_tree(1) and invert_tree(3) first. Both 1 and 3 are 
leaves — no children, so they just return themselves immediately (the base case 
bottoms out here). Back at node 2: left_inverted = 1, right_inverted = 3 → 
set 2.left = 3, 2.right = 1. Node 2 returns itself, now shaped 3 ← 2 → 1.

invert_tree(7) does the same with its leaves 6 and 9: sets 7.left = 9, 7.right = 6. 
Returns node 7, now shaped 9 ← 7 → 6.

Back at the root: left_inverted = the now-mirrored subtree rooted at 2 
(holding 3 and 1), right_inverted = the now-mirrored subtree rooted at 7 
(holding 9 and 6). Set 4.left = right_inverted (the 7-subtree), 4.right = left_inverted 
(the 2-subtree).

Final tree:

        4
      /   \
     7     2
    / \   / \
   9   6 3   1

Matches the expected [4,7,2,9,6,3,1] exactly.



"""