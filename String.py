#!/usr/bin/env python
# coding: utf-8

# ### String

# In[1]:


s = "Python is a good language"
t = "Its is good for data science"


# In[3]:


type(s)


# In[4]:


print(s)


# In[5]:


print("Hello", 12, "Who are you?", 67.54)


# In[6]:


v = s+ " "+t
print(v)


# In[9]:


price = 12
s = "The price of this book"
v = s+ " is: " + str(price)


# In[10]:


print(v)


# In[11]:


print(s, "is:", price)


# In[12]:


a = """Hello Mr. Black-D3vil.
Why are you not practicing for Samsung Hackathon?
Please be prepare for it."""


# In[13]:


print(a)


# In[16]:


print("""
THe following options are available:
            -a    :does nothing
            -b    :also does nothing
""")


# In[18]:


a = "Game of programming"
print(a[3:8])
print(a[-8:-3])

print(len(a))
print(len(a[3:8]))


# In[19]:


s = "How are you and who are you"
print(s[6])


# In[20]:


type(s[5])


# In[21]:


s[3:9]


# In[22]:


s[-1]


# In[23]:


s[-1:-3]


# In[27]:


s[-8:]

