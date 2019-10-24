#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
openFile = open('text.txt','r')
text = openFile.read()
text


# In[2]:


output = open('output.dat','w')
output.write(text+"\n\n")
def printout(arr):
    cnt=0
    for i in arr:
        cnt+=1
        output.write(str(cnt)+ ': ' + i + '\n')
    output.write('\n\n')
        
findIN = re.findall('[^a-z^A-Z^0-9]in[^a-z^A-Z^0-9]',text,re.I)
output.write('Find "in" :\n')
printout(findIN)
 
containOR = re.findall('[a-zA-Z]*or[a-zA-Z]*',text,re.I)
output.write('Contain "or" :\n')
printout(containOR)

startON = re.findall('[^a-z^A-Z^0-9]on[a-zA-Z]*',text,re.I)
output.write('Start with "on" :\n')
printout(startON)
    
endING = re.findall('[a-zA-Z]*ing',text,re.I)
output.write('End with"ing" :\n')
printout(endING)


output.close()

