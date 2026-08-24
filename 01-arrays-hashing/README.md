# Arrays & Hashing

> Status: In progress 5/8 Blind 75 problems solved (Contains Duplicate, Valid Anagram, Two Sum, Group Anagrams, Product of Array Except Self). Top K Frequent Elements started (`problems/frequent_element.py`, empty). Valid Sudoku and Longest Consecutive Sequence not started.

## What it is

An **array** (Python `list`) is contiguous, index-addressable memory — O(1) random access, O(n) insert/delete in the middle. A **hash map/set** (`dict`/`set`) trades that ordering for near O(1) average lookup, insert, and delete by hashing keys to a bucket. Most of this topic is about noticing when a hash map can replace a nested loop.

## Where it's applied

Anything sequential and index based (lists, strings, buffers) uses arrays by default. Hash maps show up whenever the question is "have I seen this?", "how many times?", or "what belongs with what?" deduplication, frequency counts, grouping by a computed key.

## Complexity cheat sheet

Array: index O(1), search O(n), append O(1) amortized, mid insert/delete O(n).
Hash map/set: insert/lookup/delete O(1) average, O(n) worst case (collisions) O(n) space.

## Patterns actually used across the problems below

Four patterns keep reappearing worth naming explicitly since spotting *which one applies* is the real skill:

1. **Seen-before / complement lookup** — walk once, check a hash set/map for "have I seen this?" or "have I seen the value that completes this?" instead of a nested loop. Used in Contains Duplicate and Two Sum.
2. **Frequency counting** — hash map of value → count, built in one pass. Used in Valid Anagram (and will drive Top K Frequent Elements once that's finished).
3. **Canonical key hashing** — when the thing you're grouping isn't directly comparable, hash by a computed key that *is* identical across the group (sorted letters, for anagrams). Used in Group Anagrams.
4. **Prefix/suffix accumulation** — precompute a running result left-to-right and right-to-left instead of recomputing a range from scratch each time. Used in Product of Array Except Self.

## Problems solved

| Problem | File | Pattern | Brute force | Optimized | Key idea |
|---|---|---|---|---|---|
| Contains Duplicate | `problems/duplicate.py` | Seen-before lookup | O(n²) / O(1) | O(n) / O(n) | Hash set answers "seen before?" in O(1), killing the inner loop. |
| Valid Anagram | `problems/valid_anagram.py` | Frequency counting | O(n log n) / O(n) | O(n) / O(1)* | Anagramness is about letter *counts*, not order sorting pays for order you don't need. |
| Two Sum | `problems/two_sum.py` | Complement lookup | O(n²) / O(1) | O(n) / O(n) | Rearrange `a + b == target` into `b == target - a`, then ask the hash map "does the partner already exist?" |
| Group Anagrams | `problems/group_anagrams.py` | Canonical key hashing | O(n²·k log k) / O(n·k) | O(n·k log k) / O(n·k) | Two anagrams aren't equal as strings, but their sorted letters form is use that as the dict key. |
| Product of Array Except Self | `product_array.py` | Prefix/suffix accumulation | O(n²) / O(1) | O(n) / O(1)** | `output[i]` = running product from the left × running product from the right, each built incrementally in one pass. |

\* bounded by alphabet size, not truly constant. \*\* excluding the output array itself.

## Still to do

- [ ] Top K Frequent Elements — `problems/frequent_element.py` (frequency counting + bucket sort, since sorting by frequency is overkill when frequency is bounded by n)
- [ ] Valid Sudoku — frequency counting across rows/cols/3x3 boxes at once
- [ ] Longest Consecutive Sequence — set-based existence check to find true sequence starts in O(n)

## Notes / gotchas (from working through these)

- **Valid Anagram's length check isn't just a speed-up.** Without it, `s = "ab"`, `t = "a"` slips through as `True` — the second loop only checks that every letter in `t` exists in `s`'s counts, it never confirms `t` used up *all* of `s`'s letters. The length check forces the comparison both ways.
- **`counts.get(ch, 0) + 1`** is doing the "treat missing key as 0" job without the default, the first time a letter shows up it'd raise `KeyError`.
- **Group Anagrams' key choice matters for cost, not just correctness** — `''.join(sorted(s))` costs `O(k log k)` per string; a 26-length character-count tuple would get the same correctness in `O(k)` instead, since it skips the sort. Worth trying as a follow-up variant.
- `product_array.py` currently sits at the topic root rather than in `problems/` like the others — harmless, just inconsistent with the rest; move it in whenever convenient.