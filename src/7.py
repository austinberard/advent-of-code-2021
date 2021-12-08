def find_fuel_to_move_part_1(origin, pos_list):
  tot_fuel = 0
  for idx in range(len(pos_list)):
    distance = abs(origin - idx)
    tot_fuel += pos_list[idx]*distance
  return tot_fuel

def find_fuel_to_move_part_2(origin, pos_list):
  tot_fuel = 0
  for idx in range(len(pos_list)):
    distance = abs(origin - idx)
    tot_fuel += int((distance*(distance+1)) / 2) * pos_list[idx]
  return tot_fuel

if __name__ == '__main__':

  test_case = None
  with open("../Data/day-7.txt", 'r') as f:
    lines = f.readlines()
    test_case = [int(x) for x in lines[0].strip().split(',')]

  sorted_crabs = sorted(test_case)
  max_pos = max(sorted_crabs)
  pos_list = [0] * (max_pos + 1)
  for c in sorted_crabs:
    pos_list[c] += 1

  min_fuel_cost_1 = None
  for idx in range(len(pos_list)):
    if min_fuel_cost_1 is None:
      min_fuel_cost_1 = find_fuel_to_move_part_1(idx, pos_list)
    else:
      min_fuel_cost_1 = min(min_fuel_cost_1, find_fuel_to_move_part_1(idx, pos_list))
  print(min_fuel_cost_1)

  min_fuel_cost_2 = None
  for idx in range(len(pos_list)):
    if min_fuel_cost_2 is None:
      min_fuel_cost_2 = find_fuel_to_move_part_2(idx, pos_list)
    else:
      min_fuel_cost_2 = min(min_fuel_cost_2, find_fuel_to_move_part_2(idx, pos_list))
  print(min_fuel_cost_2)