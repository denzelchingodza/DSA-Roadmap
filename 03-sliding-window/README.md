# Sliding Window

> Status: In progress 3/4 core Blind 75 problems solved (Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters, Longest Repeating Character Replacement). Minimum Window Substring not started.

## What it is

Sliding window is like two pointers, but both pointers move in the same direction rather than toward each other. You maintain a window (a continuous chunk of the array or string) marked by a left and right boundary. The technique is sliding the window one step at a time, incrementally updating whatever you're tracking as elements enter on the right and leave on the left.

There are two types:

1. **Fixed size window** — the window's width never changes (e.g. find the max sum of any 3 consecutive elements). You add one element on the right, drop one on the left, every step.
2. **Variable size window** — the window grows and shrinks based on a condition (e.g. finding the longest substring with no repeated characters). You expand the right until the window breaks some rule, then shrink from the left until it's valid again, tracking the best window seen along the way. This is what almost all the problems use.

## Where it's applied

Any "best/longest/shortest contiguous subarray or substring satisfying some condition" problem: max profit from one buy/sell, longest run without a repeat, longest run where you're allowed to fix up to k mismatches, smallest window containing a required set of characters.

## Complexity cheat sheet

Sliding window: `O(n)` — this is the whole point. Each element is added to the window and removed from the window at most once each across the entire run, so even though it looks like nested loops (an outer loop for right, an inner-ish loop for left), the total number of pointer moves across the whole algorithm is bounded by `2n`, not `n²`.

## Core algorithms / patterns

Imagine physically sliding a window frame along a strip of film, one frame at a time. Instead of picking the frame up and re-examining everything inside it from scratch every time you move it, you just look at what's newly visible on the right edge and what just scrolled off the left edge, and update your running picture incrementally. The "brute force → optimized" leap in every sliding window problem is exactly this: stop recomputing the whole window's property from zero every time, and instead maintain it incrementally as the window edges move.

## Problems solved

| Problem | File | Window type | Brute force | Optimized | Key idea |
|---|---|---|---|---|---|
| Best Time to Buy and Sell Stock | `problems/max_profit.py` | Growing only window | O(n²) / O(1) | O(n) / O(1) | For any sell day, the best buy day is always the minimum price seen so far carry one running value forward instead of checking every pair. |
| Longest Substring Without Repeating Characters | `problems/length_of_long_substring.py` | Variable window | O(n²) / O(n) | O(n) / O(n) | Grow right while characters stay unique; on a duplicate, shrink from the left just enough to remove it, not the whole window. |
| Longest Repeating Character Replacement | `problems/character_replacement.py` | Variable window | O(n²) / O(1) | O(n) / O(1) | A window is valid when `width - most frequent character count <= k`. `max_freq` is deliberately never decreased on shrink — it only needs to be a safe upper bound, not exact. |

## Still to do

- [ ] Minimum Window Substring — variable window tracking a full required-character-count dictionary, not just a single condition; the hardest of the four core problems here

## Notes / gotchas (from working through these)

- **Indentation changes what a loop means.** The brute force in `character_replacement.py` had `return best` sitting one level too far in inside the outer loop instead of after it so it returned after checking only the very first starting index instead of trying them all. Same category of bug as the Valid Anagram length check lesson: where a line sits relative to a loop is part of the logic, not just style.
- **Give brute force and optimized functions the same name within a file**, so the second definition cleanly overwrites the first — different names (like `character_replacement` vs `character_replacements`) mean you can accidentally keep calling the buggy version without noticing.
- `max_freq` never being decremented in Longest Repeating Character Replacement is the subtlest idea in this topic so far worth re-deriving by hand if it ever stops making sense: it only has to be a safe *upper bound* on the best window seen, not the true count of the current window.
