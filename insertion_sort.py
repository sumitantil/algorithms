import random
A = [2,4,3,1,5]

for i in range(1000000000):
    A.append(random.randint(0,1000000))

def ins_sort_iter(A):
    n = len(A)
    if n<1:
        return A
    
    for i in range(n):
        j=i
        while(j>0 and A[j-1]>A[j]):
            A[j-1],A[j]= A[j],A[j-1]
            j= j-1

    return A
print(ins_sort_iter(A))


A = [2,4,3,1,5]

def insert(A,v):
    if A==[]:
        return[v]
    
    elif v>=A[-1]:
        return (A+[v])
    else: 
        return insert(A[:-1],v)+A[-1:]

def ins_sort_rec(A):
    n = len(A)
    if n<1:
        return A
    
    L= insert(ins_sort_rec(A[:-1]),A[-1])
    return L
print(ins_sort_rec(A))
    


