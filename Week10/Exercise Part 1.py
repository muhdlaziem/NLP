#!/usr/bin/env python
# coding: utf-8

# ## Exercise Part 1

# #### 'Fighting animals could be dangerous'

# In[1]:


import nltk


# In[2]:


grammar1 = nltk.CFG.fromstring("""
S ->  VP VP
NP ->  N
VP ->  V VP | V | NP VP | AP
AP -> ADJ | VP ADJ
N -> 'animals'
V ->  'Fighting' | 'could' | 'be'
ADJ ->  'dangerous'
""")


# In[3]:


sent1 = 'Fighting animals could be dangerous'
sent1 = sent1.split()
parser = nltk.ChartParser(grammar1)


# In[4]:


for tree in parser.parse(sent1):
    print(tree)


# #### 'Visiting relatives can be tiresome'

# In[5]:


grammar2 = nltk.CFG.fromstring("""
S -> VP VP
NP -> Det N | Det N PP | 'I'
VP -> V N | VP AP | V V
AP -> ADJ
N -> 'relatives'
V -> 'Visiting' | 'can' | 'be'
ADJ -> 'tiresome'
""")


# In[6]:


sent2 = 'Visiting relatives can be tiresome'
sent2 = sent2.split()
parser = nltk.ChartParser(grammar2)


# In[7]:


for tree in parser.parse(sent2):
    print(tree)

