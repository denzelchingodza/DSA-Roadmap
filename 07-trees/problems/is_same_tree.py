# Given the roots of two binary trees p and q, write a function to check if they are the same or not

# two binaries are said to be the same if they are structurally identical,
# and the nodes have the same value 

def is_same_tree(p, q):
    if not p and not q:
        return True 

    if not p or not q:
        return False 
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


"""
Trace — the false case

p = [1,2], q = [1,null,2]:

p:      1              q:      1
       /                        \
      2                          2
At the root: p=1, q=1. Neither is empty, values match (1 == 1). Move on to check both children: is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right).
Left side: p.left = 2, q.left = None. This hits if not p or not q: — p is a real node (2), q is None. Exactly one of them is empty → returns False immediately.
Because of and, the moment the left side comes back False, the whole expression is False — Python doesn't even need to check the right side (this is called short-circuiting).

Final answer: False. Correct — node 2 sits on the left in p but on the right in q, so the shapes genuinely don't match even though both trees "contain the same numbers."
"""
