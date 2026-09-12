# Binary Search

> Status: Core topic complete — 5/5 problems solved (Binary Search, Search a 2D Matrix, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, Koko Eating Bananas). Time Based Key-Value Store and Median of Two Sorted Arrays left for a follow-up round.

## What it is

Binary Search is what you get when your data has enough order that checking one point lets you throw away half of everything else with certainty. Instead of scanning left to right, you jump to the middle, compare, and eliminate an entire half in one move. Do that repeatedly and you cut `n` items down to 1 in about `log₂(n)` steps — for a million items, that's roughly 20 comparisons instead of a million.

The two flavors covered here: searching an actual sorted array (Binary Search, Search a 2D Matrix, the two rotated-array problems), and searching a range of possible answers where "works / doesn't work" flips exactly once as you slide across the range (Koko Eating Bananas). Same tool, different target.

## Where it's applied

Anywhere data is sorted (or "sorted enough" — rotated but still structured) and you need to find a value or boundary faster than a linear scan. Also applies to any "find the smallest/largest value that satisfies some condition" problem, even when there's no array at all to search — as long as the condition is monotonic (once true, stays true as you move in one direction).

## Complexity cheat sheet

Binary search: `O(log n)` time, `O(1)` space (iterative version — no extra memory beyond a couple of index variables). Compare against the brute-force linear scan every problem here starts from: `O(n)`. The gap between `O(n)` and `O(log n)` is the entire point of this topic.

## Core algorithms / patterns

Every problem here is one of two shapes: **search an array** (narrow `left`/`right` boundaries around a sorted or rotated-sorted array until you land on the target or a boundary value), or **search an answer range** (narrow boundaries around a range of possible answers, using a "does this value work?" check instead of a direct comparison). Recognizing which shape you're in is most of the battle — the boundary-narrowing logic itself is nearly identical either way.

## Problems solved

| Problem | File | Pattern | Key idea |
|---|---|---|---|
| Binary Search | `problems/binary_search.py` | Classic array search | Compare the middle element to the target, discard the half that can't contain it, repeat. |
| Search a 2D Matrix | `problems/search_matrix.py` | Array search, flattened index | Treat the grid as one long sorted list without physically flattening it — `mid // cols` and `mid % cols` convert a flat position into a row and column. |
| Find Minimum in Rotated Sorted Array | `problems/find_min.py` | Array search, rotated | Compare the middle to the RIGHT boundary — if middle is bigger, the rotation point (minimum) is to the right; otherwise it's at or before the middle. |
| Search in Rotated Sorted Array | `problems/search_rotated.py` | Array search, rotated | One half around the middle is always properly sorted — identify which one, then check if the target's value falls inside that half's range. |
| Koko Eating Bananas | `problems/koko.py` | Binary search on the answer | Search the range of possible eating speeds, not the piles themselves — if a speed finishes in time, every faster speed also does, which is what makes the range searchable. |

## Still to do

- [ ] Time Based Key-Value Store — design problem (same flavor as Min Stack) using binary search over a sorted list of timestamped entries
- [ ] Median of Two Sorted Arrays — hardest problem in this topic, save for after more practice

## Notes / gotchas

- **`while left < right` vs `while left <= right` changes what gets checked.** The classic Binary Search needs `<=`, because when only one element remains (`left == right`), that element still needs to be checked — using `<` skips it, and the bug only shows up on edge cases like a target that happens to be the very last element considered. Find Minimum in Rotated Sorted Array correctly uses `<` instead, but for a different reason: there, `left` and `right` are converging toward the *same* answer position rather than searching for a match, so the loop is meant to stop exactly when they meet, with the answer read off afterward.
- **In Koko Eating Bananas, the direction you move `left` and `right` in has to match which way "too slow" and "too fast" point.** If the current speed is too slow (needs more hours than allowed), the fix is a *faster* speed, so `left` must move up, past the current speed — not down. Moving it the wrong direction doesn't just give a wrong answer here, it can leave `left` and `right` stuck without ever converging, hanging the function in an infinite loop — worth testing any binary-search-on-the-answer solution against a case where the middle value fails, specifically to check the boundary moves the direction you expect.
- Search in Rotated Sorted Array only needs to know which HALF is cleanly sorted at each step (via comparing `nums[left]` to `nums[mid]`) — it never needs to know where the rotation point actually is, which is a common instinct to fight since Find Minimum trains you to look for that point directly.
