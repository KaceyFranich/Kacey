#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Exercise 0
def github() -> str:
    """
    Returns a link to my new Github account
    """

    return "https://github.com/KaceyFranich/Kacey>"
link = github()
print(link)


# In[14]:


# Exercise 1
import numpy as py
import pandas as pa
import scipy as sp
import matplotlib as mpl
import seaborn as sea


# In[15]:


# Exercise 2
def evens_and_odds(n: int) -> dict:
    """
    evens sums all even numbers within the range (0,n) by seeing if i is divisible by 2
    odds sums all odd numbers within the range by seeing if i is dvisible by 2. If not, it sums
    my_dict is a dictionary of the sums of the even and odd numbers
    """
    evens = sum(i for i in range(0, n) if i % 2 == 0)
    odds = sum(i for i in range(0, n) if i % 2 != 0)
    my_dict = {'evens': evens, 'odds':odds}
    return my_dict
print(evens_and_odds(4))


# In[16]:


# Exercise 3
from typing import Union
from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """
    datetime_1 and 2 convert the strings into datetime object
    date_diff finds the difference between the two dates
    """
    datetime_1 = datetime.strptime(date_1, '%Y-%m-%d')
    datetime_2 = datetime.strptime(date_2, '%Y-%m-%d')
    date_diff = abs((datetime_1 - datetime_2).days)
    if out == 'float':
        return date_diff
    else:
        return f"There are {date_diff} days between the two dates"

print(time_diff('2020-01-01', '2020-01-02', 'float'))
print(time_diff('2020-01-01', '2020-01-02', 'string'))


# In[17]:


# Exercise 4
def reverse(in_list: list) -> list:
    """
    Start with an empty list for the reverse list
    for loop that appends in_list to the reverse list using -1 as the step in the range
    """
    reverse_list = []
    for i in range(len(in_list) - 1, -1, -1):
        reverse_list.append(in_list[i])
    
    return reverse_list

print(reverse(['a', 'b', 'c']))


# In[26]:


# Exercise 5
import numpy as np
def prob_k_heads(n: int, k: int) -> float:
    """
    Let's use the binomial distribution formula that we learned in class to find binomial probability
    """
    singleflip_prob = 0.5
    prob = np.math.comb(n, k) * (singleflip_prob ** k) * ((1 - singleflip_prob) ** (n - k))
    return prob
print(prob_k_heads(1,1))

