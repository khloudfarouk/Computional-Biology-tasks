#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install pyopenms')


# In[2]:


from pyopenms import *


# In[6]:


seq="VAKA"
moFull=0
for i in range(0,len(seq)):
    Q=seq[i]
    x = AASequence.fromString(Q)
    moFull=moFull+x.getMonoWeight()
    print(moFull)
sequance = AASequence.fromString(seq)
print("Sequence:", sequance)

Mfull = sequance.getMonoWeight()

print("Monoisotopic mass of M is = ", Mfull)


# In[ ]:




