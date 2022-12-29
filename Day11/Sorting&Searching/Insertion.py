def insertionSort(array): #[9,5,1,4,3]
    for step in range(1, len(array)): # --- We will start from 1st index 
        key = array[step] #-- 5 array[1]=5  key =5
        j = step - 1 # -- 0    j=0    
        while j >= 0 and key < array[j]: #---> Comparing values in left side of key # -- j=0 >=0 =0>=0 =true& 5<9 ture  
            array[j + 1] = array[j] # array[1] =9
            j = j - 1 
        array[j + 1] = key # --- We will start from 2st index as key 
    
data = [9, 5, 1, 4, 3]
print('Input Array before Using Insertion Sort:')
print(data)
insertionSort(data)
print('Sorted Array Using Insertion Sort in Ascending Order:')
print(data)