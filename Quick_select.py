def swap(lst,frm,to):
  temp = lst[frm]
  lst[frm] = lst[to]
  lst[to] = temp

def partition(lst,left,right,pivotIndex):
  pivotValue = lst[pivotIndex]
  swap(lst,pivotIndex,right)
  storeIndex = left
  for i in range(left,right):
    if lst[i] < pivotIndex:
      swap(lst,i,storeIndex)
      storeIndex += 1
  swap(lst,storeIndex,right)
  return storeIndex

def quickSelect(lst,left,right,k):
  k = k-1
  if left == right:
    return lst[left]
  pivotIndex  = right
  pivotIndex = partition(lst,left,right,pivotIndex)
  if pivotIndex == k:
    return lst[pivotIndex]
  elif pivotIndex < k:
    return quickSelect(lst,pivotIndex+1,right,k)
  else:
    return quickSelect(lst,left,pivotIndex-1,k)

print(quickSelect([0,-1,4,5,2,8],0,5,2))  
