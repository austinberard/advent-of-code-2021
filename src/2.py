
if __name__ == '__main__':
  hor = aim = depth = 0
  with open("../Data/day-2.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
      split_line = line.split()
      direction = split_line[0]
      amount = int(split_line[1])
      if direction == "forward":
        hor += amount
        depth += aim*amount
      elif direction == "down":
        aim += amount
      elif direction == "up":
        aim -= amount
  print(hor*depth)
        

  