def find_low_points(nums):
  low_pts = []
  for idx, n in enumerate(nums):
    if idx == 0:
      if n < nums[idx+1]:
        low_pts.append(n)
    elif idx == len(nums)-1:
      if n < nums[idx-1]:
        low_pts.append(n)
    else:
      if nums[idx-1] > n and n < nums[idx+1]:
        low_pts.append(n)
  print(low_pts)
  return low_pts


if __name__ == '__main__':
  inputs_list = []
  with open("../Data/day-9.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
      inputs_list.append([int(x) for x in line.strip()])
  
  tot = 0
  for num_list in inputs_list:
    low_points = find_low_points(num_list)
    for pt in low_points:
      tot += 1 + pt
  print(tot)
