# Algorithms reference

The techniques I should be able to reproduce from memory, in clean canonical form.
Scope: the [NeetCode](https://neetcode.io) roadmap **up to and including Trees** —
arrays & hashing, two pointers, sliding window, stack, binary search, linked lists, trees.

## Why three sections and not one list

These are not the same *kind* of thing, and they are practised differently:

| Section | What it is | How you reproduce it |
|---|---|---|
| [01 — Data structures](01-data-structures.ipynb) | Linked list, binary tree, stack/queue/counter | Memorise the **construction** — node class, traversal, dummy head |
| [02 — Algorithms](02-algorithms.ipynb) | Binary search, BFS, DFS, tree traversals | Memorise **verbatim** — one canonical form, typed identically every time |
| [03 — Patterns](03-patterns.ipynb) | Sliding window, two pointers, fast & slow, monotonic stack, prefix sums | Memorise the **skeleton** — the loop shape is fixed, the body changes per problem |
| [04 — Cheat sheet](04-cheat-sheet.ipynb) | Complexity table, problem-shape → technique lookup, gotchas | Skim before a session |

Sliding window is a *pattern* — there's no single correct implementation, only a shape.
Linked lists are a *data structure* (the node and traversal) plus *patterns* (fast & slow,
dummy head). Both belong here; labelling them correctly is what makes the drill work.

## How to use

Each notebook is self-contained — open any one cold and run it top to bottom. Structure
classes are the first code cell of the topic that needs them, and imports sit at the top of
the first cell that uses them; there is no shared setup cell.

Each topic is one `##` header giving complexity and the key insight, followed by one code
cell per function. There are no demo prints — the point is to read the implementation and
then reproduce it, not to watch it run.

Sections are numbered from 1 within each notebook, so the cheat sheet refers to them as
`02 §1`, `03 §3`, and so on.

## Contents

**01 — Data structures:** 1. linked list (traversal · dummy head · reverse · merge sorted) ·
2. binary tree construction · 3. stack, queue, counting

**02 — Algorithms:** 1. binary search (exact match · lower bound · on the answer space ·
2D matrix) · 2. tree DFS (recursive · iterative) · 3. tree BFS · 4. depth and the bottom-up
return

**03 — Patterns:** 1. two pointers (opposite ends · sort-and-fix) · 2. fast & slow pointers ·
3. sliding window (fixed · variable · with counts) · 4. monotonic stack · 5. prefix & suffix ·
6. hash set membership · 7. tree recursion · 8. BST

**04 — Cheat sheet:** which technique for which problem shape · complexity table · gotchas ·
Python idioms

## Not covered

Past Trees on the roadmap, so deliberately out of scope for now: tries, heaps / priority
queues, backtracking, graphs, dynamic programming.
