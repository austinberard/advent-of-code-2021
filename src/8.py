# 1478

def parse_inputs(line):
  inputs = line.strip().split('|')[0].split(' ')[:-1]
  return inputs

def parse_outputs(line):
  outputs = line.strip().split('|')[1].split(' ')[1:]
  return outputs

def solve_line(inputs, outputs):
  answer = [ [] for i in range(7)]
  sorted_inputs = sorted(inputs, key=lambda x: len(x))

  print(sorted_inputs)
  print(answer)

if __name__ == '__main__':
  inputs_list = []
  output_list = []
  with open("../Data/day-8-sample.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
      inputs_list.append(parse_inputs(line))
      output_list.append(parse_outputs(line))

  for inputs, outputs in zip(inputs_list, output_list):
    solve_line(inputs, outputs)