#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())
i = 1
while (i <= n):
    print(i**2)
    print("This is iteration number: ", i)
    i += 1
print("Loop Done")


# In[2]:


n = int(input("Max iteration : "))
i = 1
while i < n:
    if i%2 == 0:
        print(i)
    else:
        pass
    i += 1
print("Done")


# In[2]:


n = 10
i = 1
while True:
    if i%9 == 0:
        print("Inside If: ", i+1)
        break
    else:
        print("Inside else: ", i+1)
        i = i+1
print("done")


# In[ ]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("Inside If: ", i+1)
        i += 1
        continue
        print("This is not printed")
        break
print("done")


# In[1]:


L = []
for i in range(0,10,2):
    print(i+1)
    L.append(i**2)
print(L)


# In[5]:


s = {"apple", 4.9, "cherry"}
i = 1
for x in s:
    print(x)
    i += 1
    if i == 3:
        break
    else:
        pass
else:
    print("Loop terminates with success")
print("Outside the Loop")


# In[10]:


D = {"A":10, "B":-19, "C":"abc"}
for x in D:
    print(x, ":", D[x])


# In[ ]:




