# Trees

> Status: In progress (3/8 core problems solved)

## What it is

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Where a linked list is a straight line (each node points to exactly one next node), a tree lets a node branch — a binary tree means each node points to at most two children, called `left` and `right`. The top node is the root, nodes with no children are leaves, and any node plus everything hanging below it is a subtree.

Two words that come up constantly: depth (how far a node is from the root, counting edges) and height (how far a node is from its furthest leaf below it). A tree with n nodes arranged as evenly as possible has height around log₂(n) — that's the property the whole topic is built on.

A Binary Search Tree (BST) is a binary tree with one extra rule bolted on: for every node, everything in its left subtree is smaller, everything in its right subtree is bigger. That single rule is what turns "search the whole tree" into "you can throw away half the tree at every step" — the same idea as Binary Search, just shaped like a tree instead of an array.

## Where it's applied

- File systems — folders containing folders containing files
- The HTML DOM — every element nested inside a parent element
- Database indexes (B-trees) — how databases find a row without scanning every row
- Decision trees in machine learning
- Compilers — parsing code into an Abstract Syntax Tree
- Autocomplete-style structures (a close cousin, Tries, is its own topic right after this one)

## Complexity cheat sheet

| Operation | Balanced tree | Unbalanced tree (worst case) |
|---|---|---|
| Search (BST) | O(log n) | O(n) |
| Insert (BST) | O(log n) | O(n) |
| Delete (BST) | O(log n) | O(n) |
| Any full traversal | O(n) | O(n) |

Space: O(n) to store the tree itself, plus O(h) for the call stack during recursion, where h is the height — O(log n) if balanced, but O(n) in the worst case (a tree where every node only has one child is really just a linked list wearing a disguise, and recursion depth suffers exactly like that).

## Core algorithms / patterns

- **DFS (recursion/stack)** — going deep before wide. Three flavors depending on when you "visit" the current node relative to its children: preorder (node, then left, then right), inorder (left, then node, then right — for a BST this visits every value in sorted order, which is a huge deal), postorder (left, then right, then node — used when you need to know about both children before you can decide anything about the current node; root is visited last).
- **BFS (queue)** — going wide before deep. Process the tree one full level at a time. This is how you get "level order" output, or answer anything shaped like "leftmost/rightmost node at each depth."
- **Divide and conquer.** Almost every tree problem has the same skeleton: solve it for the left subtree, solve it for the right subtree, then combine those two answers to get the answer for the current node. Recursion isn't optional here, it's the natural shape of the data.
- **Exploiting the BST property.** If you know left-is-smaller/right-is-bigger, you can compare the target to the current node and immediately know which single side to continue into, skipping the other half entirely — same shrink-the-search-space idea as Binary Search.

## Blind 75 problems mapped to this topic

- [x] Invert Binary Tree
- [x] Maximum Depth of Binary Tree
- [x] Same Tree
- [ ] Subtree of Another Tree
- [ ] Binary Tree Level Order Traversal
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element in a BST
- [ ] Lowest Common Ancestor of a BST
- [ ] Binary Tree Maximum Path Sum (harder — later)
- [ ] Serialize and Deserialize Binary Tree (harder — later)
- [ ] Construct Binary Tree from Preorder and Inorder Traversal (harder — later)

## Notes / gotchas

- Always handle `if not root: return ...` first — the base case for an empty subtree is where almost every bug starts.
- Recursion depth equals tree height. A badly unbalanced tree can, in the worst case, get close to Python's recursion limit.
- The BST speedup only exists if your code actually compares against `node.val` to pick a side — a plain tree traversal on a BST gets none of that benefit.
