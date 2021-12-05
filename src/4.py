from collections import deque
from pprint import pprint

def column(matrix, i):
    return [row[i] for row in matrix]

def sum_board(board):
  tot = 0
  for row in board:
    for item in row:
      if item != '-1':
        tot += int(item)
  return tot
        

def check_board(board, number):
  for idx_r, row in enumerate(board):
    for idx_c, _ in enumerate(row):
      if board[idx_r][idx_c] == number:
        board[idx_r][idx_c] = '-1'
        return

def check_winner(board):
  for row in board:
    if row == ['-1']*5:
      return True
  for i in range(5):
    col = column(board, i)
    if col == ['-1']*5:
      return True
  return False


if __name__ == '__main__':
  numbers_to_call = deque()
  boards = []
  with open("../Data/day-4.txt", 'r') as f:
    lines = f.readlines()
    numbers_to_call = deque(lines[0].strip().split(','))
    cur_board = []
    for idx, line in enumerate(lines):
      if idx < 2:
        continue
      if line == '\n':
        boards.append(cur_board)
        cur_board = []
      else:
        nums = [s for s in line.split() if s.isdigit()]
        cur_board.append(nums)
    boards.append(cur_board) 

  boards_deque = deque()
  for board in boards:
    boards_deque.append(board)

  while numbers_to_call:
    number = numbers_to_call.popleft()
    for i in range(len(boards_deque)):
      check_board(boards_deque[i], number)
      if check_winner(board):
        print("winner")
        answer = sum_board(boards_deque[i]) * int(number)
        print("Answer is: {}".format(answer))
        boards_deque.remove(boards_deque[i])
    pprint(boards_deque)