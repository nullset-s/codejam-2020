#!/usr/bin/env python
# coding: utf-8

# In[1]:

def latin(I,N,arr):
    sum=0
    for i in range(N):
        sum+=arr[i][i]
    I=I+1
    
    col=0
    row=0
    
    for a in range(N): 
        
        if check([row[a] for row in arr]):            #For column element
            col+=1
    for array in arr:                      #For row element
        if check(array): 
            row+=1
    print("Case #"+str(I)+": "+str(sum)+" "+str(row)+" "+str(col))

def check(array): 
    for i in range(0,len(array)):
        for j in range(1, len(array)): 
            if j!=i:                                #should not check for itself
                if array[i]==array[j]: 
                    return True 
    return False

import numpy as np
T=int(input().strip()) #strip() remove space

for t in range(0,T):
    N=int(input())
    arr=np.zeros((N,N),dtype=int)
    for i in range(0,N):
        R=(input().split(' '))
        for j in range(0,N):
            arr[i,j]=R[j]

    latin(t,N,arr)  


# In[ ]:




