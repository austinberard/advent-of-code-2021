from pprint import pprint

if __name__ == '__main__':
  days = 256
  fish = [0] * 10
  with open("../Data/day-6.txt", 'r') as f:
    lines = f.readlines()
    fish_to_add = [int(x) for x in lines[0].strip().split(',')]

    for item in fish_to_add:
      fish[item] += 1


  while days > 0:
    new_fish_list = fish # is this a copy? or an alias
    for idx, num_of_fish in enumerate(fish):
      if num_of_fish == 0:
        continue
      if idx == 0:
        new_fish_list[9] += num_of_fish
        new_fish_list[0] -= num_of_fish
        new_fish_list[7] += num_of_fish
      else:
        new_fish_list[idx] -= num_of_fish
        new_fish_list[idx-1] += num_of_fish
    fish = new_fish_list
    days -= 1

  print(sum(fish))
  