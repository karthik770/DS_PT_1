def heapify(arr, n, i):  # ([12,6,10,5,1,9],6,3)
      largest = i  # 3
      l = 2 * i + 1 # l= (2*3)+1   = 6 +1 =7 --> l=7
      r = 2 * i + 2  # r= (2*3) +2  = 6+2 =8
      if l < n and arr[i] < arr[l]:
          largest = l
      if r < n and arr[largest] < arr[r]:
          largest = r
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)

def heapSort(arr): #[12,6,10,5,1,9]
      n = len(arr) # n=6
      for i in range(n//2, -1, -1): # (3,-1,-1)
          heapify(arr, n, i)   # ([12,6,10,5,1,9],6,3)
      for i in range(n-1, 0, -1):
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)


arr = [12,6,10,5,1,9]
heapSort(arr) 
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')

