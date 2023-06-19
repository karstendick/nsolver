import json
from itertools import product
from copy import deepcopy

with open('example1.json', 'r') as f:
  puzzle = json.load(f)

nrows = puzzle['nrows']
ncols = puzzle['ncols']
row_clues = puzzle['row_clues']
col_clues = puzzle['col_clues']

BLANK = ' '
FILLED = '1'
EMPTY = '0'
solution = [BLANK for _ in range(nrows * ncols)]


def get_row(solution, r, nrows, ncols):
  starti = r * ncols
  endi = starti + ncols
  ret = []
  for i in range(starti, endi):
    ret.append(solution[i])
  return ret

def set_row(solution, row, r, nrows, ncols):
  starti = r * ncols
  endi = starti + ncols
  ri = 0
  for i in range(starti, endi):
    solution[i] = row[ri]
    ri += 1
  return solution

def get_col(solution, c, nrows, ncols):
  starti = c
  endi = nrows * ncols
  ret = []
  for i in range(starti, endi, ncols):
    ret.append(solution[i])
  return ret

def set_col(solution, col, c, nrows, ncols):
  starti = c
  endi = nrows * ncols
  ri = 0
  for i in range(starti, endi, ncols):
    solution[i] = col[ri]
    ri += 1
  return solution

def count_blank(grid):
  count = 0
  for cell in grid:
    if cell == BLANK:
      count += 1
  return count

def is_solved(grid):
  return count_blank(grid) == 0

def gen_clue(grid):
  clue = []
  n = 0
  for cell in grid:
    if cell == FILLED:
      n += 1
    elif cell == EMPTY:
      if n == 0:
        pass
      elif n > 0:
        clue.append(n)
        n = 0
  if n > 0:
    clue.append(n)
  return clue

def is_clue_matched(clue, grid):
  return gen_clue(grid) == clue

def and_candidates(grid, candidates):
  ret = deepcopy(grid)
  for i, cell in enumerate(ret):
    if cell != BLANK:
      continue
    can_set = set([candidate[i] for candidate in candidates])
    if len(can_set) == 1:
      answer = can_set.pop()
      ret[i] = answer
  return ret

def solve_row(clue, grid):
  candidates = []
  num_blank = count_blank(grid)
  bstrings = product('01', repeat=num_blank)
  for bstring in bstrings:
    candidate = []
    bi = 0
    for cell in grid:
      if cell == BLANK:
        candidate.append(bstring[bi])
        bi += 1
      else:
        candidate.append(cell)
    if is_clue_matched(clue, candidate):
      candidates.append(candidate)
  return and_candidates(grid, candidates)


def solve_rows(row_clues, solution):
  for r in range(nrows):
    soln_row = solve_row(row_clues[r], get_row(solution, r, nrows, ncols))
    set_row(solution, soln_row, r, nrows, ncols)
  return solution

def solve_cols(col_clues, solution):
  for c in range(ncols):
    soln_row = solve_row(col_clues[c], get_col(solution, c, nrows, ncols))
    set_col(solution, soln_row, c, nrows, ncols)
  return solution

def print_grid(grid, nrows, ncols):
  print('---')
  for r in range(nrows):
    row = get_row(grid, r, nrows, ncols)
    print(str(row))
  print('---')

for i in range(nrows * ncols):
  solution = solve_rows(row_clues, solution)
  print_grid(solution, nrows, ncols)
  solution = solve_cols(col_clues, solution)
  print_grid(solution, nrows, ncols)
  print()
  print()
  if is_solved(solution):
    print('Solved it!')
    break
