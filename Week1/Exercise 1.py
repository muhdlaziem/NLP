#!/usr/bin/env python
# coding: utf-8

# In[1]:


dictionary ={}
def exercise1(filename):
    openFile= open(filename,"r")
    readFile = openFile.read()
    
    #create dictionary with frequency
    for word in readFile.split():    
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    #print dictionary an the frequecy of each word
    print(dictionary,'\n')
    
    #print the ocurrence of "of"
    print ("The occurence of 'of' is ", dictionary["of"],'\n')
    
    #print words which end with "ly"
    print("The words that ends with 'ly' are:")
    idx=0;
    for word in readFile.split():    
        if word.endswith('ly'):
            idx+=1
            print(idx,': ',word)
    


exercise1("recipe_Ital_115.txt")
    

