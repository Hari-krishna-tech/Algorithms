def num_of_rot(rotated_sorted_lst):
  n = len(rotated_sorted_lst)
  low = 0
  high = n - 1

  while low <= high:
    mid = low + (high-low)//2
    next = (mid+1)%n
    pre = (mid-1+n)%n
    if rotated_sorted_lst[mid] <= rotated_sorted_lst[next] and rotated_sorted_lst[mid] <= rotated_sorted_lst[pre]:
      return mid
    if rotated_sorted_lst[mid] <= rotated_sorted_lst[high]:
      high = mid-1
      continue
    if rotated_sorted_lst[mid] >= rotated_sorted_lst[low]:
      low = mid+1

  return -1
    


print(num_of_rot([4,5,6,7,0,1,2,3]))


