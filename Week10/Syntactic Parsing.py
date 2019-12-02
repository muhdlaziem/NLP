#!/usr/bin/env python
# coding: utf-8

# ## Parsing with NLTK

# In[1]:


import nltk


# In[2]:


grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my' | 'the' 
N -> 'elephant' | 'pajamas' | 'station'
V -> 'shot'
P -> 'in' | 'at'
""")


# In[3]:


sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(grammar)


# In[4]:


for tree in parser.parse(sent):
    print(tree)


# ## Exercise

# In[5]:


grammar1 = nltk.CFG.fromstring("""
S ->  VP VP
NP ->  N
VP ->  V VP | V | NP VP | AP
AP -> ADJ | VP ADJ
N -> 'animals'
V ->  'Fighting' | 'could' | 'be'
ADJ ->  'dangerous'
""")


# In[6]:


sent1 = 'Fighting animals could be dangerous'
sent1 = sent1.split()
parser = nltk.ChartParser(grammar1)


# In[7]:


for tree in parser.parse(sent1):
    print(tree)


# In[8]:


sent


# In[9]:


grammar2 = nltk.CFG.fromstring("""
S -> VP VP
NP -> Det N | Det N PP | 'I'
VP -> V N | VP AP | V V
AP -> ADJ
N -> 'relatives'
V -> 'Visiting' | 'can' | 'be'
ADJ -> 'tiresome'
""")


# In[10]:


sent2 = 'Visiting relatives can be tiresome'
sent2 = sent2.split()
parser = nltk.ChartParser(grammar2)


# In[11]:


for tree in parser.parse(sent2):
    print(tree)


# In[ ]:




