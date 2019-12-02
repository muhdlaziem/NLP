#!/usr/bin/env python
# coding: utf-8

# ## Probabilistic Parsed Trees with NLTK Chart Parser

# In[1]:


import nltk


# In[2]:


grammar = nltk.PCFG.fromstring("""
S -> NP VP [0.8] | Aux NP VP [0.1] | VP[0.1]
NP -> Det Nominal [0.6] | Pronoun [0.2] | Proper-Noun [0.2]
Nominal -> Noun [0.3] | Nominal Noun [0.2] | Nominal PP [0.5]
VP -> Verb [0.3] | Verb NP [0.2] | VP PP [0.5]
PP -> Prep NP [1.0]
Det -> 'the' [0.6] | 'a' [0.2] | 'that' [0.1] | 'is' [0.1]
Verb -> 'book' [0.5] | 'include' [0.2] | 'prefer' [0.3]
Noun -> 'book' [0.1] | 'flight' [0.5] | 'meal' [0.2] | 'money' [0.2]
Proper-Noun -> 'Houston' [0.8] | 'NWA' [0.2]
Prep -> 'from' [0.25] | 'to' [0.25] | 'near' [0.1] | 'through' [0.2] | 'on' [0.2]
""")


# In[3]:


print(grammar)


# In[4]:


from nltk.parse import pchart
parser = pchart.InsideChartParser(grammar)


# In[5]:


sent = 'book the flight through Houston'


# In[6]:


trees = parser.parse(sent.split())


# In[7]:


for t in trees:
    print(t)


# ## PCFG Grammar & Bracketed Trees

# In[8]:


from nltk.draw.tree import draw_trees
from nltk.parse import pchart


# In[9]:


for t in trees:
    draw_trees(t)


# In[ ]:




