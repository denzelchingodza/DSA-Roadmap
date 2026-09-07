# Stack

> Status: In progress — 3/4 problems solved so far (Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation). Daily Temperatures and Car Fleet (monotonic stack) not started.

## What it is

A stack is a collection where you can only add to, or remove from, one end — the "top." Last in, first out (LIFO): whatever you pushed most recently is the first thing that comes back off. In Python, you don't need a special class for this — a plain list already works as a stack, using `.append()` to push and `.pop()` to pop (both O(1) at the end of a list).

The reason this earns its own topic, distinct from arrays: a huge number of problems have a hidden "most recent thing I haven't resolved yet" structure to them, and a stack is the data structure that tracks that naturally, without you having to reinvent it with indices and loops.

## Where it's applied

Anything with nested or matching structure — parentheses/brackets, HTML tags, undo history, function call chains (this is literally how your program's call stack works under the hood). Anything with a "most recent unresolved thing" shape — evaluating expressions, tracking the next larger/smaller value relative to where you currently are, backtracking through a path. Anywhere you'd naturally say "go back to the last thing I was doing" — that's a stack.

## Complexity cheat sheet

Push, pop, and peek (look at the top without removing it) are all O(1) — you're only ever touching one end. Most stack-based algorithms end up O(n) overall, because even though there's often a loop with something that looks like it could be nested (a while popping inside a for), each element is pushed once and popped at most once across the entire run — same total-work argument as sliding window's two pointers, just with a stack instead of indices.

## Core algorithms / patterns

Picture a stack of plates. You can only ever take the top plate off, or put a new plate on top. If you need to know what's underneath the top plate, you can't just look — you'd have to remove plates one at a time until you get there, and by definition, whatever you remove last was put there first. Every stack problem is some version of: "keep a pile of things I'm not done with yet, and the moment I find out what resolves the most recent one, deal with it, then check what's now on top."

## The process

1. Is there a "most recent unresolved thing" in this problem? If yes, stack. If the order that gets resolved doesn't matter, it's not a stack problem.
2. What exactly goes onto the stack? Not always the raw input element — sometimes it's a modified version, a pair, an index.
3. What condition causes something to come off the stack? State it in plain words — like Sliding Window's "validity rule," just for popping instead of shrinking.
4. What do you do at the very end? Is a non-empty stack a valid outcome, an error, or still-unprocessed work?
5. Movement logic follows from 2–4: walk the input once, apply step 3 (pop if it applies), then step 2 (push, if appropriate), check step 4 at the end.

## Problems solved

| Problem | File | Pattern | Key idea |
|---|---|---|---|
| Valid Parentheses | `problems/valid_paranthesis.py` | Matching/nesting | Closing bracket must match whatever's currently on top — LIFO is exactly what makes "most-recently-opened closes first" checkable. |
| Min Stack | `problems/min_stack.py` | Design — precompute at push time | Push `(value, min_so_far)` pairs instead of just values — popping automatically "reverts" the minimum for free, no recomputation needed. |
| Evaluate Reverse Polish Notation | `problems/eval.py` | Direct real-world stack use | Numbers get pushed; an operator pops the two most recent operands, computes, and pushes the result back for future operators to use. |

## Still to do

- [ ] Daily Temperatures — monotonic stack (keep indices in decreasing-temperature order, popping whenever a warmer day breaks that order)
- [ ] Car Fleet — monotonic stack applied to arrival times
- [ ] Largest Rectangle in Histogram — hardest of this topic, save for last

## Notes / gotchas

- In Evaluate Reverse Polish Notation, operand order matters for `-` and `/`: the second pop is always the operand that appeared earlier in the original expression, so it goes on the **left** — `right - left`, not `left - right`, would silently flip the sign.
- Min Stack's trick (store extra state alongside each stack entry, computed once at push time) is worth remembering as its own reusable idea — it comes up again in harder stack problems.
