# Linked List

> Status: Core topic complete — 5/5 problems solved (Merge K Sorted Lists left for later)

## What it is
A linked list stores data as a chain of separate nodes, where each node holds
a value plus a pointer to the next node. Unlike an array, nodes are NOT
sitting next to each other in memory the only thing connecting them is
those pointers.

That's the whole tradeoff versus an array: you lose instant index access
(getting to node 5 means walking through nodes 0-4 first, no shortcuts),
but you gain cheap insertion/removal — deleting a node you're already
standing at is just rewiring two pointers (O(1)), no shifting of other
elements required.
A **singly** linked list only has `next` pointers (forward only). A
**doubly** linked list also has `prev` pointers, so you can walk backward too.

## Where it's applied
- Browser back/forward history
- Undo/redo chains in editors
- "Next track" queues in music apps
- Hash map collision handling (each bucket is a small linked list)
- LRU Cache (linked list + hash map together covered later in the roadmap)
- OS memory allocators tracking free blocks

## Complexity cheat sheet
| Operation | Array | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) |
| Search by value | O(n) | O(n) |
| Insert at front | O(n) | O(1) |
| Insert at end | O(1) amortized | O(1) with a tail pointer, else O(n) |
| Insert/delete in middle | O(n) | O(1) once you're standing at the node — getting there is still O(n) |
| Space | O(n), tight | O(n) + one pointer per node overhead |

## Core algorithms / patterns
- **Fast & slow pointers (Floyd's technique)** — one pointer moves 1 node at
  a time, the other moves 2. Used to find the middle of a list in one pass,
  detect cycles (fast laps slow if there's a loop), and find the nth node
  from the end (offset the pointers by n, then walk together).
- **Reversal** — walk forward one node at a time, flipping each node's
  `next` pointer to point backward instead. Must save the original `next`
  in a temp variable BEFORE overwriting it, or the rest of the list is lost.
- **Dummy head node** — when the head itself might change (removing the
  first node, building a list by merging), create a fake node pointing at
  the real head, do all the work relative to the dummy, return `dummy.next`
  at the end. Removes head-specific edge cases entirely.
- **Merging** — same idea as the merge step of merge sort: keep a pointer
  into each list, always take the smaller current value, advance that
  pointer, repeat until one list runs out, then attach the rest of the other.


## Blind 75 problems mapped to this topic
- [x] Reverse Linked List
- [x] Merge Two Sorted Lists
- [x] Linked List Cycle
- [x] Reorder List
- [x] Remove Nth Node From End of List
- [ ] Merge K Sorted Lists (may slot in after Heap/Priority Queue instead)

## Notes / gotchas
- Always save `node.next` in a temp variable before overwriting it, or the
  rest of the list is lost mid-reversal.
- Any function that builds new nodes (Merge Two Sorted Lists, Remove Nth
  Node From End) needs its own `ListNode` class with a real `__init__` in
  the same file -- an empty `class ListNode:` with no constructor will
  crash the moment you try to create a node.
- Watch indentation around a `class` block closely: a function accidentally
  indented under `class ListNode:` silently becomes a method (and needs
  `self`) instead of a standalone function -- keep the class and your
  solution functions at the same, top level, not nested.
- A loop body line that ends up outside the loop it belongs to (usually
  from a stray dedent) doesn't just give a wrong answer here -- since the
  pointer never advances, the loop never ends. Caught this exact bug twice
  today (Merge Two Sorted Lists, Remove Nth Node From End) before it hit
  GitHub.

