def linearSearch(array, x): #[2, 4, 0, 1, 9] , 1
    n = len(array) # n=5
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

# array = [2, 4, 0, 1, 9]
# x = 1
array=[]
a=int(input("Enter the Array count: "))
for i in range(0,a):
    va=int(input())
    array.append(va)

x=int(input("Enter search key : "))
print(array)
print(x)
result = linearSearch(array, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
