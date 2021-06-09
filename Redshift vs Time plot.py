#!/usr/bin/env python
# coding: utf-8

# In[2]:


# plotting Redshift (z) as a function of time (t)

# start by importing the following packages
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# begnning of code

data_by_Jillian = np.loadtxt("C:/Users/John/Desktop/Code/times.list")  # list provided by Jillian. Type "C:" for Windows
time_data = data_by_Jillian[:, 0]  # time data (measured in giga year)
redshift_data = data_by_Jillian[:, 1]  # redshift data (z)
plt.plot(time_data, redshift_data, '.')
plt.xlabel("Time (giga-annum)")  # x-axis label
plt.ylabel("Redshift")  # y-axis label
plt.title("Redshift as Function of Time")  # graph's name
plt.show()

# end of code


# In[ ]:




