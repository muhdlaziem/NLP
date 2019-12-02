#!/usr/bin/env python
# coding: utf-8

# ## Probabilistic Parsed Trees with NLTK Viterbi Parser

# In[1]:


import nltk


# In[2]:


grammar = nltk.PCFG.fromstring("""
S -> NP VP [0.9] | VP [0.1]
NP -> Det A N [0.1] | NP PP [0.3] | PropN [0.2] | Det [0.1] | Det PropN [0.3]
A -> ε [0.6] | Adj A  [0.4]
PP -> Prep NP [1.0]
VP -> VP NP [0.1] | VP PP [0.3] | VP V [0.3] | V NP PP [0.3]
Det -> 'the' [0.6] | 'a' [0.2] | 'that' [0.1] | 'is' [0.1]
Prep -> 'from' [0.25] | 'to' [0.25] | 'near' [0.1] | 'through' [0.15] | 'on' [0.15] | 'in' [0.1]
Adj -> 'handsome' [0.3] | 'gorgeous' [0.3] | 'pretty' [0.4]
PropN -> 'John' [0.3] | 'horse' [0.4] | 'stable' [0.3]
V -> 'liked' [0.5] | 'disliked' [0.5]
""")


# In[3]:


# from nltk.parse import pchart
# parser = pchart.InsideChartParser(grammar)
parser = nltk.ViterbiParser(grammar)


# In[4]:


print(grammar)


# In[5]:


sent = 'John liked the horse in the stable'


# In[6]:


trees = parser.parse(sent.split())


# In[7]:


for i in parser.parse(sent.split()):
    print(i)


# In[8]:


from nltk.draw.tree import draw_trees
from nltk.parse import pchart
for i in trees:
    draw_trees(i)

