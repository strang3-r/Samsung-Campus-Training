#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import logging.conf

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is debug message')

# In[4]:


logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('Hello from helper')


# In[5]:


# Create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')


# In[6]:


# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)


# In[7]:


formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)


# In[8]:


logger.addHandler(stream_h)
logger.addHandler(file_h)


# In[9]:


logger.warning('this is a warning')
logger.error('this is an error')

