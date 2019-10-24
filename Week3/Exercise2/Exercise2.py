#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.book import *


# In[2]:


import nltk

dat = open('nltk_out.dat','w')

def percent(word,text):
    #convert to lowercase
    fdist = nltk.FreqDist(ch.lower() for ch in text if ch.isalpha())
    dat.write('The occurence of "'+ word +'" in the text is: '+str(fdist[word.lower()])+'\n')
    dat.write('The percentage of "'+ word +'" in the text is: '+ str(round((fdist[word.lower()])/len(text)*100,5)) +'% \n')
    setText = set(text)
    dat.write('The words that less than or equal to 5 are: \n')
    cnt=0;
    for w in setText:
        if(len(w)<=5):
            cnt+=1
            dat.write(str(cnt) + ': ' + w +'\n')
    dat.write('\n\n')
    

percent("moby",text1)
percent("Moby",text1)
percent("monstrous",text1)
percent("and",text2)
percent("corpus",text5)
dat.close()


# In[ ]:




