#!/usr/bin/env python
# coding: utf-8

# ## Now we extract B40 Residents

# In[1]:


import re    
openFile = open('residents.dat','r')
text = openFile.read()
text


# In[2]:


b40dat = re.findall('[a-zA-Z]*[\s][0-6][0-9][0-9][0-9][0-9][0-9]-10-[0-9]*[\s][0-9]*[\s][0-9]*[\s]',text,re.I)
b40dat


# In[3]:


with open('b40.dat', 'w') as b40:
    for i in range(len(b40dat)):
        b40.write(b40dat[i])


# In[ ]:




