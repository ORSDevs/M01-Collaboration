#!/usr/bin/env python
# coding: utf-8

# In[8]:


seconds_in_minute = 60
minutes_in_hour = 60

seconds_per_hour = seconds_in_minute * minutes_in_hour
print(seconds_per_hour, "seconds")


# In[9]:


seconds_per_hour = 3600
hours_in_day = 24

seconds_in_day = seconds_per_hour * hours_in_day
print(seconds_in_day, "seconds")


# In[10]:


seconds_per_day = 86400
seconds_per_hour = 3600

result = seconds_per_day / seconds_per_hour
print(result)


# In[11]:


seconds_per_day = 86400
seconds_per_hour = 3600

result_int = seconds_per_day // seconds_per_hour
print(result_int)


# In[ ]:




