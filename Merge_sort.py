from array import array
import time

def merge_sort(A):
    #base case
    if len(A)<=1:
        return A

    left_arr = A[:len(A)//2]
    right_arr = A[len(A)//2:]

    #merge 
    L=merge_sort(left_arr)
    R=merge_sort(right_arr)

    F = merge(L,R)

    return F
    
def merge(A,B):
    m,n = len(A),len(B)
    C,i,j,k = [],0,0,0
    while k< m+n:
        if i == m:
            C.extend(B[j:])
            k += n-j
            
        elif j == n:
            C.extend(A[i:])
            k += m-i
        
        elif A[i]<B[j]:
            C.append(A[i])
            k+=1
            i+=1
        else:
            C.append(B[j])
            k+=1
            j+=1

    return C
import random
A = [2,4,3,1,5]

l1 = time.perf_counter()
for i in range(10000000):
    A.append(random.randint(0,10000000))
n1 = time.perf_counter()


l2 = time.perf_counter()
print(merge_sort(A))
n2 = time.perf_counter()
print(n1-l1)
print(n2-l2)
