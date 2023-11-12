#!/usr/bin/env python
# coding: utf-8

# # Dataframe creation (List)

# In[35]:


import pandas as pd
list_fufu = [
            ['fish', 'banana', 'biscuit', 'garri'],
            ['clamora', 'python', 'lawrence', 'bros J']
            ]


# In[36]:


data_frame = pd.DataFrame(list_fufu)


# In[37]:


print(data_frame)


# # Dataframe manipulation

# In[74]:


garri_dictionary = {
                    'Amala': ['carbohydrate', 'semovita'],
                    'Garri': ['red garri', 'Garri-1']
                    }


# In[75]:


data_frame_1 = pd.DataFrame(garri_dictionary)
print(data_frame_1)


# # Selection from dataframe (loc/iloc)

# In[76]:


print(data_frame_1.iloc[1])


# In[77]:


print(data_frame.loc[1])


# # How to manipulate rows

# In[78]:


data_frame.loc[0,1] = 'triple ohh'


# In[79]:


print(data_frame)


# # How to manipulate columns
# 

# In[81]:


data_frame_1['laptops'] = ['macbook', 'hp']
print(data_frame_1)


# In[ ]:





# In[ ]:




