def count_ones(list_with_ones):
  tot = 0
  for item in list_with_ones:
    if item == 1:
      tot += 1
  return tot



if __name__ == '__main__':
  bits_list = []
  with open("../Data/day-3.txt", 'r') as f:
    lines = f.readlines()
    bit_len = len(lines[0].strip())
    for bit in range(bit_len):
      bits_list.append([])
    for line in lines:
      for bit in range(bit_len):
          bits_list[bit].append(int(line[bit]))

  bit_len = len(bits_list)
  gamma = [0] * bit_len

  for bit in range(bit_len):
    ones_count = count_ones(bits_list[bit])
    if ones_count > (len(bits_list[bit]) // 2):
      gamma[bit] = 1
  print(gamma)
  gamma = int(''.join(map(str, gamma)), 2)
  epsilon = ~gamma
  print(epsilon*gamma)