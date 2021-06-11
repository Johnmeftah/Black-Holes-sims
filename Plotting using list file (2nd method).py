#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import the good stuff
import numpy as np 
import matplotlib.pyplot as plt

# beginning of code
X, Y = [], [] # initializes the list of coordinates X and Y as empty lists.
for line in open("C:/Users/John/Desktop/times.list", "r"): # define a loop that will iterate each line of your file.
  values = [float(s) for s in line.split()] # split the current line around empty characters to form a string of tokens. 
                                            #Those tokens are then interpreted as floating points.
  X.append(values[0]) 
  Y.append(values[1]) # the values stored in values are appended to the lists X and Y.

plt.plot(X, Y) # starting plotting X and Y.
plt.xlabel("Time (giga-annum)") # give your x-axis a label 
plt.ylabel("Redshift") # give your y-axis a label
plt.title("Redshift as Function of Time") # give your plot a title
plt.show() # enjoy
# end of code


# In[ ]:




