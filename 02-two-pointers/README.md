# Two Pointers

> Status: Not started — 0/5 Blind 75 problems solved. Stub files created for Valid Palindrome, Two Sum II, and Container With Most Water (`problems/`, all empty).

## What it is

Two Pointers isn't a data structure it's a technique applied *to* arrays and strings. Instead of one index walking through the array, you keep **two** indices active at once and move them according to a rule based on what you're looking for. Almost every problem here looks like it needs to check every pair (`O(n²)`), but a sorted array or a symmetric structure (like a palindrome) lets you eliminate whole ranges of possibilities with each step instead of checking them one by one.

Two shapes show up constantly:

**Opposite-direction (converging) pointers** — one starts at the front, one at the back, moving toward each other. Used for palindrome checks, sorted-array pair sums, and container/water problems. This is the shape this topic focuses on.

**Same-direction (fast/slow) pointers** — both start at the front, moving at different rates. Shows up more in Linked List and Sliding Window (which is really Two Pointers with both pointers moving the same direction).

## Where it's applied

Anywhere the input is sorted (or can be sorted), or has a symmetric/mirrored structure to exploit: checking palindromes, finding pairs/triples that sum to a target in a sorted array, merging two sorted arrays, and any "shrink the search space from both ends" problem.

## Complexity cheat sheet

Two pointers over an array: `O(n)` time, `O(1)` space each pointer moves at most `n` times total and never moves backward, so total work across the whole run is linear even though it "looks like" checking pairs.

If sorting is required first: `O(n log n)` for the sort (dominates), then `O(n)` for the two-pointer pass.

## The core idea

Picture two people at opposite ends of a sorted line of numbers, each holding a finger on one number. At every step they look at how their two numbers compare, and exactly one of them steps inward. Because the line is sorted, moving the left finger right can only *increase* whatever you're tracking, and moving the right finger left can only *decrease* it so you always know with certainty which direction fixes the problem, and never need to backtrack. That certainty is what replaces the nested loop.

## Problems mapped to this topic

| Problem | File | Pattern | Key idea |
|---|---|---|---|
| Valid Palindrome | `problems/valid_palindrome.py` | Converging pointers | Compare mirrored characters from both ends inward instead of building a reversed copy trades O(n) space for O(1). |
| Two Sum II (sorted input) | `problems/two_sum.py` | Converging pointers, sortedness as certainty | Sum too small → move left pointer up; too big → move right pointer down. Same O(n) time as the hash-map Two Sum, but O(1) space since sortedness replaces the lookup table. |
| Container With Most Water | `problems/max_area.py` | Converging pointers, greedy proof | Water = width × shorter wall. Moving the taller wall can only shrink width while the limiting height stays the same, so it's provably never better always move the shorter wall's pointer. |
| 3Sum | *(not started)* | Sort + fix one, two-pointer the rest | Sort the array, fix one number, then run the Two Sum II pattern on the remaining two skip duplicate values while sliding to avoid repeat triples. |
| Trapping Rain Water | *(not started)* | Converging pointers with running max | Water trapped at each position is bounded by the shorter of the tallest wall seen so far on each side track both running maxes while converging inward. |

## Notes / gotchas

- Valid Palindrome needs an inner skip loop on each side to jump over non alphanumeric characters before comparing easy to forget the `left < right` bound inside that inner loop too, which can let the pointers run past each other.
- Two Sum II returns **1-indexed** positions per the problem spec easy to forget the `+1` when returning.
- Container With Most Water: the greedy "always move the shorter wall" step is the part worth re deriving by hand before coding it it's not obvious until you trace why moving the taller wall can never help.
