# nsolver

A python program to solve [nonogram puzzles](https://en.wikipedia.org/wiki/Nonogram).

## Usage

```bash
python3 nsolver.py
```

## Algorithm

The solver alternates between the rows and columns, considering a single row (or column) at a time in isolation. It continues doing this until the puzzle is solved.

For a single row (or column), it generates all the possible ways to fill in the blank cells and then filters those that match the given clue. If all of these candidates agree on any cells, then those cells are solved.

Generating all the possible ways to fill in a single row (or column) takes 2^N time, where N is the length. That's exponential time. Even for a 15x15 puzzle, it takes over 1.5 seconds to run on my laptop. (The code takes advantage of an iterator to avoid keeping all 2^N candidates in memory.)

Although considerable speedups are no doubt possible, solving nonograms is [NP-complete](https://en.wikipedia.org/wiki/Nonogram#Nonograms_in_computing), so there's a limit to how much improvement is possible.

## Acknowledgements

Thanks to [Gary Rosenzweig](https://garyrosenzweig.com/about.html) for creating [Nonograms Unlimited](https://clevermedia.com/apps/NonogramsUnlimited.html), a free iOS game for playing nonogram puzzles. My love of this game is what inspired me to write this solver.

Thanks also to [Activity Workshop](https://activityworkshop.net/puzzlesgames/nonograms/example.html) for the example nonogram puzzles.
