def sortAndCount(A):
    if len(A)<=1:
        return A,0
    
    (L, countL) = sortAndCount( A[:len(A)//2] )

    (R, countR) = sortAndCount(A[len(A)//2:])

    (F, countF) = mergeAndCount(L,R)

    return (F, countL+countR+countF)

def mergeAndCount(L,R):
    m,n = len(L), len(R)
    C,i,j,k,count = [],0,0,0,0

    while k<m+n :
        if i == m:
            C.extend(R[j:])
            k += n-j
        elif j == n:
            C.extend(L[i:])
            k += m-i
        elif L[i]<R[j]:
            C.append(L[i])
            i,k = i+1, k+1
        else:
            C.append(R[j])
            j,k,count = j+1, k+1,count + m-i
    
    return (C,count)

A = [2,4,3,1,5]

print(sortAndCount(A))

    