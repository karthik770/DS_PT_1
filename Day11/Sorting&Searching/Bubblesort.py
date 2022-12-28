def bubbleSort(array):
  for i in range(len(array)):
    swapped = False #---> Memory counter
    for j in range(0, len(array) - i - 1): #---->[1,5,4,2,8]
      if array[j] >  array[j + 1]:
        temp = array[j]   #---> jar1 jar2  jar3(tempjar) 
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break

data = [5,1,4,2,8]
print('Input Array before Using Bubble Sort:')
print(data)
bubbleSort(data)
print('Sorted Array Using Bubble Sort in Ascending Order:')
print(data)