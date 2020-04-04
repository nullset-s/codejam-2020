#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Dept(j):
    
    temp=0
    S=''
    for x in j:
       
        x=int(x)
        if x>temp:
            S=S+('('*(x-temp))
       
        if x < temp:
            S=S+(')'*(temp-x))
       
        S=S+str(x)
        x=int(x)
        temp=x

    S=S+')'*x
    return S

T=int(input().strip()) #strip() remove space
for i in range(0,T):
    j=(input())
    k=Dept(j)
    print("Case #"+str(i+1)+": "+k)

