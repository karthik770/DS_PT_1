def partition(array, low, high): #([8,7,6,1,0,9,2], 0 , 6)
  pivot = array[high]  # array[6]  ->pivot= 2
  i = low - 1  # i= -1
  for j in range(low, high): # --> we are going to set the value less than pivot at left & greater on right 
    if array[j] <= pivot: # array[0] 8 <= 2 --> False 
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1]) #2, 8
  return i + 1

def quickSort(array, low, high): #([8,7,6,1,0,9,2], 0 , 6)
  if low < high: # 0< 6 --> True
    pi = partition(array, low, high) #([8,7,6,1,0,9,2], 0 , 6)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)


data = [8,7,6,1,0,9,2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1) #  ([8,7,6,1,0,9,2], 0 , 6)
print('Sorted Array in Ascending Order:')
print(data)