import time,random
# Function to print array element
def printArray(arr, N):
     
    # Traverse the array
    for i in range(N):
        print(arr[i], end = ' ')
         
# Function to sort the array in O(N)
def sortArray(arr, N):
     
    i = 0
     
    # Traverse the array
    while i < N:
         
        # If the current element is
        # at correct position
        if arr[i] == i + 1:
            i += 1
         
        # Else swap the current element
        # with it's correct position
        else:
             
            # Swap the value of
            # arr[i] and arr[arr[i]-1]
            temp1 = arr[i]
            temp2 = arr[arr[i] - 1]
            arr[i] = temp2
            arr[temp1 - 1] = temp1
    return arr

A=[]
l1 = time.perf_counter()
for i in range(10000):
    A.append(random.randint(0,10000000))
n1 = time.perf_counter()


l2 = time.perf_counter()
print(sortArray(A,9999))
n2 = time.perf_counter()
print(n1-l1)
print(n2-l2)