import numpy as np
from pprint import pprint

def parse_lines(lines):
  line_segments = []
  for line in lines:
    split_line = line.strip().split(' ')
    x1, y1 = split_line[0].split(',')
    x2, y2 = split_line[2].split(',')
    if x1 == x2 or y1 == y2:
      line_segments.append([int(x1), int(y1),
                            int(x2), int(y2)])
  return line_segments

def find_xmax(line_segments):
  xmax = 0
  for line in line_segments:
    if line[0] > xmax:
      xmax = line[0]
    if line[2] > xmax:
      xmax = line[2]
  return xmax

def find_ymax(line_segments):
  ymax = 0
  for line in line_segments:
    if line[1] > ymax:
      ymax = line[1]
    if line[3] > ymax:
      ymax = line[3]
  return ymax

def mark_line_on_grid(line, grid):
  x1, y1, x2, y2 = line

  start_x = min(x1, x2)
  start_y = min(y1, y2)
  end_x = max(x1, x2)
  end_y = max(y1, y2)

  for x in range(start_x, end_x+1):
    for y in range(start_y, end_y+1):
        grid[y][x] += 1

def find_number_of_intersecting_lines(grid):
  tot = 0
  for row in grid:
    for item in row:
      if item > 1:
        tot += 1
  return tot



if __name__ == '__main__':
  line_segments = None
  with open("../Data/day-5.txt", 'r') as f:
    line_segments = parse_lines(f.readlines())

  xmax = find_xmax(line_segments) + 1
  ymax = find_ymax(line_segments) + 1 

  grid = np.zeros((xmax+1, ymax+1))

  for line in line_segments:
    mark_line_on_grid(line, grid)
  
  intersections = find_number_of_intersecting_lines(grid)
  print(intersections)