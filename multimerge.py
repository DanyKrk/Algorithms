def merge(left, right):
  result = [0]*(len(left)+len(right))
  l_i = 0
  r_i = 0
  index = 0
  while l_i < len(left) and r_i < len(right):
    if left[l_i] <= right[r_i]:
      result[index] = left[l_i]
      l_i += 1
    else:
      result[index] = right[r_i]
      r_i += 1
    index += 1
  while l_i < len(left):
    result[index] = left[l_i]
    l_i += 1
    index += 1
  while r_i < len(right):
    result[index] = right[r_i]
    r_i += 1
    index += 1
  return result

def merge_lists(lists):
  while len(lists) > 1:
    new_lists = []
    for i in range(0, len(lists), 2):
      if i+1 < len(lists):
        res = merge(lists[i], lists[i+1])
      else:
        res = lists[i]
      new_lists.append(res)
    lists = new_lists
  return lists

tab = [[1,6,11,16,21], [2,7,12,17],[3,8,13,18],[4,9,14,19],[5,10,15,20]]
print(merge_lists(tab)[0])