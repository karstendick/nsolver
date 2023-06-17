import json
from itertools import product
from copy import deepcopy

with open('example1.json', 'r') as f:
  puzzle = json.load(f)

nrows = puzzle['nrows']
ncols = puzzle['ncols']
rows = puzzle['rows']
cols = puzzle['cols']

print(puzzle)

BLANK = ' '
FILLED = '1'
EMPTY = '0'


solution = [[BLANK for i in range(ncols)] for j in range(nrows)]
print(solution)



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



print(solve_row([3], solution[0]))
print(solve_row([1], solution[0]))
print(solve_row([4], solution[0]))
print(solve_row([5], solution[0]))












