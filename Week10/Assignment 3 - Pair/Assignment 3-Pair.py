#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import string
import math
import os
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from collections import defaultdict 


# In[2]:


path = '/home/muhdlaziem/Workspace/NLP/Week8/article'
token_dict ={}
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


# In[3]:


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems  = stem_tokens(tokens, stemmer)
    return stems

for subdir, dirs, files in os.walk(path):
    for file in files:
        file_path =  subdir + os.path.sep + file
        print(file_path)
        article = open(file_path,'r')
        text = article.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(string.punctuation)
        token_dict[file] = no_punctuation


# In[4]:


tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words=['english'])
tfs = tfidf.fit_transform((token_dict.values()))


# In[5]:


feature_names = tfidf.get_feature_names()
corpus_index = [n for n in token_dict]
import pandas as pd
df = pd.DataFrame(tfs.T.todense(), index=feature_names, columns=corpus_index)

print(df)


# ## Results

# In[6]:


arr = pd.DataFrame()
strings = ['win','ringgit','trade','game','kill']
for i in df.index:
    if i in strings:
        print(i +'\n')
        print(df.loc[i])
#         arr.append(df.loc[i])
        print('\n')


# In[7]:


def k_means(tfs):
    true_k=2
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=50,n_init=1)
    model.fit(tfs)
    print("Top terms per cluster: ")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf.get_feature_names()
    
    for i in range(true_k):
        print("Cluster %d: " % i)
        for ind in order_centroids[i]:
#             print(ind)
            if(terms[ind] in strings):
            
                print(str(ind)+ ': '+ terms[ind])
k_means(tfs) 


# In[ ]:




