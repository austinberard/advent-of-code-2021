from pprint import pprint

if __name__ == '__main__':
  days = 80
  fish = None
  with open("../Data/day-6.txt", 'r') as f:
    lines = f.readlines()
    fish = [int(x) for x in lines[0].strip().split(',')]

  while days > 0:
    new_fish = []
    for idx, f in enumerate(fish):
      if f == 0:
        fish[idx] = 6
        new_fish.append(8)
      else:
        fish[idx] = f - 1
    fish += new_fish
    days -= 1

  print(len(fish)) 
  