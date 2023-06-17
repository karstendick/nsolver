import json

with open('example1.json', 'r') as f:
  puzzle = json.load(f)

print(puzzle)
