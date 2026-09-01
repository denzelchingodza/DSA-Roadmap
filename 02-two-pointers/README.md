# Two Pointers

> Status: In progress — 3/5 Blind 75 problems solved (Valid Palindrome, Two Sum II, Container With Most Water). 3Sum and Trapping Rain Water not started.

## What it is

Two Pointers isn't a data structure — it's a technique applied *to* arrays and strings. Instead of one index walking through the array, you keep **two** indices active at once and move them according to a rule based on what you're looking for. Almost every problem here looks like it needs to check every pair (`O(n²)`), but a sorted array or a symmetric structure (like a palindrome) lets you eliminate whole ranges of possibilities with each step instead of checking them one by one.

Two shapes show up constantly:

**Opposite-direction (converging) pointers** — one starts at the front, one at the back, moving toward each other. Used for palindrome checks, sorted-array pair sums, and container/water problems. This is the shape this topic focuses on.

**Same-direction (fast/slow) pointers** — both start at the front, moving at different rates. Shows up more in Linked List and Sliding Window (which is really Two Pointers with both pointers moving the same direction).

## Where it's applied

Anywhere the input is sorted (or can be sorted), or has a symmetric/mirrored structure to exploit: checking palindromes, finding pairs/triples that sum to a target in a sorted array, merging two sorted arrays, and any "shrink the search space from both ends" problem.

## Complexity cheat sheet

Two pointers over an array: `O(n)` time, `O(1)` space — each pointer moves at most `n` times total and never moves backward, so total work across the whole run is linear even though it "looks like" checking pairs.

If sorting is required first: `O(n log n)` for the sort (dominates), then `O(n)` for the two-pointer pass.

## The core idea

Picture two people at opposite ends of a sorted line of numbers, each holding a finger on one number. At every step they look at how their two numbers compare, and exactly one of them steps inward. Because the line is sorted, moving the left finger right can only *increase* whatever you're tracking, and moving the right finger left can only *decrease* it — so you always know with certainty which direction fixes the problem, and never need to backtrack. That certainty is what replaces the nested loop.

## Problems solved

| Problem | File | Pattern | Brute force | Optimized | Key idea |
|---|---|---|---|---|---|
| Valid Palindrome | `problems/valid_palindrome.py` | Converging pointers | O(n) / O(n) | O(n) / O(1) | Compare mirrored characters from both ends inward instead of building a reversed copy — trades O(n) space for O(1). |
| Two Sum II (sorted input) | `problems/two_sum.py` | Converging pointers, sortedness-as-certainty | O(n²) / O(1) | O(n) / O(1) | Sum too small → move left pointer up; too big → move right pointer down. Same O(n) time as the hash-map Two Sum, but O(1) space since sortedness replaces the lookup table. |
| Container With Most Water | `problems/max_area.py` | Converging pointers, greedy proof | O(n²) / O(1) | O(n) / O(1) | Water = width × shorter wall. Moving the taller wall can only shrink width while the limiting height stays the same, so it's provably never better — always move the shorter wall's pointer. |

## Still to do

- [ ] 3Sum — sort the array, fix one number, then run the Two Sum II pattern on the remaining two, skipping duplicate values to avoid repeat triples
- [ ] Trapping Rain Water — converging pointers with a running max height tracked on each side

## Notes / gotchas (from working through these)

- **Width formula is the easy thing to get wrong in Container With Most Water.** The gap between two pointers is `right - left`, not a fixed offset — a caught bug here was writing `j - 1` instead of `j - i` in the brute force, which happens to look plausible at a glance but silently gives wrong answers for almost every pair except when `i` is 1. Worth double-checking any "distance between two pointers" formula against a concrete example before trusting it.
- **Naming brute force and optimized functions identically (not just similarly) matters.** When the two versions have different names in the same file (e.g. `max_area` vs `max_height`), whichever name you actually call determines which logic runs — easy to accidentally keep testing against the wrong one. Matching names, so the second definition cleanly overwrites the first, keeps that from happening.
- Two Sum II returns **1-indexed** positions per the problem spec — easy to forget the `+1` when returning.
