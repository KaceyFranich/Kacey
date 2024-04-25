#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 0
def github() -> str:
    """
    returns link to my github repository
    """

    return "https://github.com/KaceyFranich/Kacey/"

print(github())


# In[1]:


#Exercise 1
import pandas as pd
import matplotlib.pyplot as plt

def load_data() -> pd.DataFrame:
    """
    define the link to the csv file as url
    read the file using read_csv
    return the df
    """
    url = 'https://lukashager.netlify.app/econ-481/data/TSLA.csv'
    df = pd.read_csv(url)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

#print(load_data().head)
dataframe = load_data()
get_ipython().run_line_magic('store', 'dataframe')
print(dataframe.head)
print(dataframe.dtypes)


# In[2]:


# Exercise 2
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('store', '-r dataframe')

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    First we need to make the strings into datetime objects
    Then create the df that is bound by the end dates
    """
    #start_date = pd.to_datetime(start)
    #end_date = pd.to_datetime(end)

    #bound_df = df['Adj Close'].loc[start:end]
    #df.index = pd.to_datetime(df.index)
    bound_df = df[(df['Date'] >= start) & (df['Date'] <= end)]
    
    plt.figure(figsize=(10, 6))
    plt.plot(bound_df['Date'], bound_df['Close'], color='blue', marker='o', linestyle='-')
    plt.title(f"Closing Price ({start} to {end})")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.tight_layout()
    plt.ylim(0,3)
    plt.show()
    
plot_close(dataframe, '2010-06-29', '2011-04-15')


# In[3]:


# Exercise 3
# import pandas as pd
# import statsmodels.api as sm
# import numpy as np

# %store -r dataframe

# def autoregress(df: pd.DataFrame) -> float:
#     """
#     I started by using the .diff() function to calculate the diff between the consecutive closing stock prices
#     I need to define the delta xt and delta xt-1 values. I'm going to define delta xt as y since it is the dependent variable
#     Then I define the delta xt-1 value as x because it is the independent variable, and I add the intercept
#     Then I use sm.OLS function to run the regression, and find the t-value of the coefficient of xt-1
#     """
#     df['Delta_xt'] = df['Close'].diff()
#     df = df.dropna()
#     y = df['Delta_xt'][:1]
#     df['Delta_xt_minus_one'] = df['Delta_xt'].shift(1, freq = 1)[:1]
#     \

#     reg = sm.OLS(y, x).fit(cov_type = 'HC1')
#     t_val = model.tvalues[1]
#     return t_val

# print(autoregress(dataframe))


# In[4]:


#Exercise 4
# import pandas as pd
# import statsmodels.api as sm
# import numpy as np
# %store -r dataframe

# def autoregress_logit(df: pd.DataFrame) -> float:
#     """
#     Some docstrings.
#     """
#     df['Delta_xt'] = df['Close'].diff()
#     y = df['Delta_xt']
#     df['Delta_xt_minus_1'] = df['Delta_xt'].shift(1)
#     x = df['Delta_xt_minus_1']

#     prob = np.exp(df['Delta_xt_minus_1']) / (1 + np.exp(df['Delta_xt_minus_1']))
#     x = sm.add_constant(prob, prepend=False)

#     logit_reg = sm.Logit((df['Delta_xt'] > 0).astype(int), x).fit()
#     t_val = logit_reg.tvalues[1]

#     return t_val

# print(autoregress_logit(dataframe))


# In[5]:


#Exercise 5
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('store', '-r dataframe')

def plot_delta(df: pd.DataFrame) -> None:
    """
    Some docstrings.
    """
    df['delta_xt'] = df['Close'].diff()
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['delta_xt'])
    plt.title('Change in Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Change in Price')
    plt.grid(True)
    plt.show()

print(plot_delta(dataframe))


# In[ ]:




