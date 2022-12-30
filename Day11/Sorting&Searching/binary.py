def binarySearch(array, x, low, high): # ([1,2,3,5,6,8],6,0,5)
    if high >= low: #5>=0
        mid = low + (high - low)//2 #  0+(5-0)//2 = (0+5)//2 =2 ---> mid =2  mid =array[2] =3
        if array[mid] == x:
            return mid # mid=array[2] =3
        elif array[mid] > x: # Left part 
            return binarySearch(array, x, low, mid-1)
        else: # Right part 
            return binarySearch(array, x, mid + 1, high) # ([1,2,3,5,6,8] , 6 , 3 , 5 )
    else:
        return -1
    
array = [1,2,3,5,6,8]
x = 6
result = binarySearch(array, x, 0, len(array)-1) 
if result != -1: 
    print("Element is present at index " + result)
else:
    print("Not found")