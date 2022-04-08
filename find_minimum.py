import time
M = ['ee','ef','eh','r','s','t','a','b','c','d','e','f','g']

def findMinimum(L):
  i=0
  while True:
    
    
    left = 0
    left_val = L[0]

    right = len(L)
    right_val = L[-1]

    mid = left+right//2
    mid_val =L[mid]

    print (left_val,mid_val,right_val)

    if len(L)==1 or len(L)==2:
      return L[-1]
    if left_val<mid_val:
      L = L[mid:]
    if left_val>mid_val:
      L = L[:mid+1]
      
    
  
    #if L[mid-1]<L[mid+1]
  
l = time.perf_counter()
K = findMinimum(M)
n = time.perf_counter()
print(K,(n-l)*(1000000))