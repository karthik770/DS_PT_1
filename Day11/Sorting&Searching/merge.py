def mergeSort(array): #  [6, 5, 12, 10, 9, 1] # [6,5,12] #[10,9,1] --> L=[10] M=[9,1] 
    if len(array) > 1: # Checking the array is greater than 1 
        r = len(array)//2  # --> 6//2 = 3   Ground /Ceiling Flooring   # r=3//2 = 1.5 =1 & 2 , L=[6] M=[5,12] 
        L = array[:r]  #---> array[:3] --> (Start from the oth index and it will ignore the 34rd index) 0-2 
                        #---> L= [6,5,12]
        M = array[r:]  # ---> array[3:] -->(start from 3 included and till the end) 3-length of array --> [10,9,1]
        mergeSort(L) # [6,5,12] 
        mergeSort(M) #[10,9,1]
        #[6][5][12][10][9][1]
        i = j = k = 0 
        while i  < len(L)  and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i] #--> swapping
                i += 1
            else: # L[i]=10 M[j]=9 
                array[k] = M[j] # -->Swapping
                j += 1
            k += 1   # ---> [6][5][12] --> 5,6,12
        while i < len(L): # Len(L) =3
            array[k] = L[i]  #[6,5,12] 
            i += 1
            k += 1
        #--> [5,6,12]
        while j < len(M): # [10,9,1]
            array[k] = M[j] 
            j += 1
            k += 1
            # [1,9,10]
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


array = [6, 5, 12, 10, 9, 1]
print('Input Array before Using Merge Sort:')
print(array)
mergeSort(array) 
print("Sorted Array Using Merge Sort in Ascending Order:")
printList(array)