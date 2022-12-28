def selectionSort(array):
    size=len(array)
    for step in range(size):
        min_idx = step # 0 / 20
        for i in range(step + 1, size): # -->12,10,15,2
            if array[i]  <  array[min_idx]:
                min_idx = i # 3
        (array[step], array[min_idx]) = (array[min_idx], array[step]) #---> swapping 
        # 2,12,10,15,20

data = [20,12,10,15,2]
print('Input Array before Using Selection Sort:')
print(data)
#size = len(data)
selectionSort(data)
print('Sorted Array Using Selection Sort in Ascending Order:')
print(data)
