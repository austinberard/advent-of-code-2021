
def increasing(list_of_nums):
  prev = None
  tot = 0
  for num in list_of_nums:
    if prev == None:
      prev = num
      continue
    if num > prev:
      tot += 1
    prev = num
  return tot

def increasing_3_sum(list_of_nums):
  tot = 0
  for idx, num in enumerate(list_of_nums):
    if idx < 3:
      continue
    if idx > len(list_of_nums)-1:
      continue
    if sum(list_of_nums[idx-2:idx+1]) > sum(list_of_nums[idx-3:idx]):
      tot += 1
  return tot


if __name__ == '__main__':
  nums = []
  with open("../Data/day-1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
      nums.append(int(line))
  print(increasing(nums))
  print(increasing_3_sum(nums))


  