A = [2,4,3,1,5]
def selection_sort(A):
    n = len(A)
    if n==0:
        return False
    for i in range(n):
        mpos = i
        for j in range(i+1,n):
            if A[j]<A[mpos]:
                mpos = j
        A[i],A[mpos] = A[mpos],A[i]
    return A

print(selection_sort(A))