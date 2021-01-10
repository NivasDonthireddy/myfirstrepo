#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello world')


# In[2]:


2 + 2


# In[4]:


5.3/5


# In[5]:


import math

math.sin(1)


# # This is a Markdown Heading 1
# ## This is Heading 2
# ### This is Heading 3
# 
# This is a **Markdown** *cell*
# 
# ````python
# 
# def sum(a,b):
#     ans  = 2+2
#     return ans
# ````
# 
# >Quotetext
# 
# Here is some fancy $\LaTeX$
# 
# $$
# \frac
# $$
# 
# 

# In[6]:


def sum(a,b):
    return a+b


# In[8]:


sum(1,6)


# In[10]:


def sum(a,b=2):
    return a + b


# In[12]:


sum(2)


# In[18]:


def sum(*var_args):
    ans = 0
    for i in var_args:
        ans += i
        
    return ans


# In[19]:


sum(1,2,3,4)


# We may have fixed arguments or Variable arguments inside the functions as in above example

# In[22]:


f = lambda x: x+2


# In[23]:


f(2)


# In[24]:


g = lambda x,y:x+y


# In[25]:


g(2,2)


# This is how the test functions work. 

# In[27]:


def test_sum():
    assert abs(sum(2,2) - 4) <= 1e-6


# In[ ]:




