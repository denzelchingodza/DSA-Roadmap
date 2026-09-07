# Recap: Arrays & Hashing → Two Pointers → Sliding Window

A checkpoint before Stack — the goal here isn't to re-teach any of this, it's to compress it into the handful of ideas that actually connect all three topics, so that when a new problem shows up, you recognize *which family it belongs to* before you start coding.

## The one idea underneath everything so far

Every problem we've worked through is the same story told three different ways: **a brute force checks every pair (or every window) from scratch, costing `O(n²)`, and the optimized version finds a way to carry information forward instead of recomputing it — costing `O(n)`.** The three topics differ only in *what kind of information gets carried forward, and how*:

- **Arrays & Hashing** carries forward a *memory* — a hash map or set answering "have I seen this?" or "what have I seen?" in O(1). You pay O(n) space to buy that memory.
- **Two Pointers** carries forward a *position* — instead of remembering values in a hash map, you exploit sortedness (or symmetry) so that a pointer's location alone tells you what you need to know. You pay nothing in extra space, but you need the input sorted or structurally symmetric first.
- **Sliding Window** carries forward a *running state* — a count, a set, a sum — that updates incrementally as one element enters and one leaves, instead of recomputing the whole window's property from scratch every time it shifts.

If you can identify *what's being carried forward* in a new problem, you've basically identified which of these three patterns to reach for.

---

## Arrays & Hashing

**Core principle:** a hash map/set trades `O(n)` memory for turning "have I seen this?" or "how many of this?" questions into O(1) lookups — killing whatever nested loop was asking those questions repeatedly.

**When you reach for it:** the question is about *existence* ("have I seen this value?"), *frequency* ("how many times does this appear?"), or *grouping* ("what belongs together?") — and there's no useful order to exploit, or the input isn't sorted and sorting it would cost more than it saves.

**The four recurring patterns:**
1. **Seen-before / complement lookup** — walk once, check a hash set/map instead of a nested loop. *(Contains Duplicate, Two Sum)*
2. **Frequency counting** — hash map of value → count, built in one pass. *(Valid Anagram)*
3. **Canonical key hashing** — group things that aren't directly comparable by hashing a computed key that *is* identical across the group. *(Group Anagrams)*
4. **Prefix/suffix accumulation** — precompute running results left-to-right and right-to-left instead of recomputing a range from scratch. *(Product of Array Except Self)*

**Complexity baseline:** hash map operations are O(1) *average*, O(n) worst case (collisions) — this is a detail worth being able to state precisely, since it's a common follow-up question.

**Problems solved (5/8):** Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Product of Array Except Self. **Still open:** Top K Frequent Elements, Valid Sudoku, Longest Consecutive Sequence.

---

## Two Pointers

**Core principle:** when the array is sorted (or has a mirrored/symmetric structure like a palindrome), two indices moving with certainty — one from each end, converging — can replace both the nested loop *and* the hash map, because sortedness itself tells you which pointer is safe to move at every step.

**When you reach for it:** the input is sorted, or can be usefully sorted, or the problem has a symmetry to exploit (front/back mirroring). This is Arrays & Hashing's "seen-before lookup" pattern, but with the lookup table replaced by geometric position — same O(n) time as the hash approach, but O(1) space instead of O(n). That trade-off (space for structure) is the single most important thing to remember about this topic.

**The two shapes:**
1. **Converging pointers** (what we covered) — one at each end, moving toward the middle. *(Valid Palindrome, Two Sum II, Container With Most Water)*
2. **Same-direction pointers** — both start at the front, move at different rates. This is the shape Sliding Window is built from.

**The reasoning tool that makes this topic click:** at every step, ask "which pointer's movement is *provably* the only one that could improve the answer?" — sortedness usually gives you certainty (Two Sum II: sum too small → only moving left can fix it), and sometimes it's a greedy proof instead (Container With Most Water: moving the taller wall can never help, so only the shorter wall's pointer is worth moving).

**Problems solved (3/5):** Valid Palindrome, Two Sum II, Container With Most Water. **Still open:** 3Sum, Trapping Rain Water.

---

## Sliding Window

**Core principle:** Sliding Window *is* Two Pointers, specifically the same-direction case — but reframed around maintaining a contiguous "window" (marked by `left` and `right`) whose contents you update incrementally, rather than pointers converging toward each other.

**When you reach for it:** the question asks for the longest/shortest/best *contiguous* subarray or substring satisfying some condition. The keyword to watch for is "contiguous" (subarray, substring, consecutive) — if elements don't need to be adjacent, this isn't the right tool.

**Fixed vs. variable width:**
- **Fixed** — window size is given upfront; you add one element on the right, drop one on the left, every step. *(Not yet covered with a dedicated problem, but this is the simpler case.)*
- **Variable** — you grow `right` greedily until the window breaks some rule, then shrink from `left` until it's valid again, tracking the best window seen along the way. *(What all three solved problems use.)*

**The process that actually derives the code** (this is the part worth re-reading before Stack, since it's the transferable skill):
1. Is it asking about a contiguous run? (filters whether Sliding Window applies at all)
2. Fixed or variable width?
3. State the window's validity rule in one plain-English sentence.
4. Decide what running state proves that rule quickly, without recomputing from scratch.
5. The movement logic (when to grow, when to shrink, when to record the answer) falls out of steps 3 and 4 almost mechanically.

**Problems solved (3/4 core):** Best Time to Buy and Sell Stock (the simplest case — a window that only ever grows, tracking a running minimum), Longest Substring Without Repeating Characters (hash set as the window's validity check), Longest Repeating Character Replacement (frequency count + a deliberately "stale" running max as a safe upper bound). **Still open:** Minimum Window Substring.

---

## How the three topics actually relate, side by side

| | What's carried forward | Cost | Needs |
|---|---|---|---|
| Arrays & Hashing | A hash map/set (memory of what's been seen) | O(n) space | Nothing — works on unsorted input |
| Two Pointers | A pointer position (proof of what's safe to skip) | O(1) space | Sortedness or symmetry |
| Sliding Window | A running window state (incremental count/sum/set) | Varies (often O(1) or bounded) | Contiguity — the answer must be a contiguous run |

Two Pointers is what you reach for when you *could* solve something with a hash map, but the input's sortedness lets you do it for free, memory-wise. Sliding Window is what Two Pointers becomes when the problem isn't "find a pair" but "find the best contiguous range."

## Bugs worth remembering (because they'll recur in new forms)

Two real bugs came up while working through these, both worth internalizing as categories, not just fixes:

- **A line's indentation is part of its logic, not just style.** Both the Valid Anagram length-check omission and the Longest Repeating Character Replacement `return` statement sitting inside the wrong loop were this same category of bug — where a line sits relative to a loop changes what the code actually does, silently.
- **An off-by-formula error in a "distance between two pointers" calculation** (`j - 1` instead of `j - i` in Container With Most Water) is easy to write and easy to miss at a glance, precisely because it still looks plausible. Worth a habit: trace any pointer-distance formula against one concrete example before trusting it.

## What's next: Stack

Stack introduces the first topic where the *data structure itself* enforces an ordering rule (last-in-first-out) that does a lot of the work for you — a different flavor of "carrying information forward" than anything above: instead of a hash map, a pointer position, or a window, you carry forward a *history*, with the guarantee that you can only ever undo it in reverse order. Worth noticing, as we get into it, whether the same "what's being carried forward, and what does that buy you" question still applies — it does, and it's a good habit to keep asking it going forward.
