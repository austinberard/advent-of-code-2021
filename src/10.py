matching = {'{': '}',
            '[': ']',
            '<': '>',
            '(': ')'}

score_map = {')': 3,
             ']': 57,
             '}': 1197,
             '>': 25137,
             '?': 0
             }

score_map_part_2 = {'(': 1,
                    '[': 2,
                    '{': 3,
                    '<': 4}

incomplete_lines = []

def complete_line(line):
  stack = []
  for ch in line:
    if ch in ['(', '<', '{', '[']:
      stack.append(ch)
    elif ch in [')', '>', '}', ']']:
      head = stack.pop()
  return stack[::-1]

def part_2_score(line):
  tot_score = 0
  for ch in line:
    tot_score *=5
    tot_score += score_map_part_2[ch]
  return tot_score

def find_first_corrupted(line):
  stack = []
  for ch in line:
    if ch in ['(', '<', '{', '[']:
      stack.append(ch)
    elif ch in [')', '>', '}', ']']:
      head = stack.pop()
      if matching[head] == ch:
        continue
      else:
        return ch
  print('inc')
  incomplete_lines.append(line)
  return '?'

if __name__ == '__main__':
  inputs_list = []
  with open("../Data/day-10.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
      inputs_list.append([x for x in line.strip()])

  # Part 1 
  tot = 0
  for code in inputs_list:
    tot += score_map[find_first_corrupted(code)]
  print('Part 1')
  print(tot)

  tot = 0
  completed = []
  scores = []
  print('Part 2')
  for line in incomplete_lines:
    scores.append(part_2_score(complete_line(line)))
  scores_sorted = sorted(scores)
  print(scores_sorted[len(scores_sorted)//2])
