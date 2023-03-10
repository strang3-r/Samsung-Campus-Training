#!/usr/bin/env python
# coding: utf-8

# ### logging

# In[13]:


import logging


# In[16]:


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M%S')


# In[17]:


logging.debug('This is a debug message')
logging.info('This is info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


# In[20]:


import helper

