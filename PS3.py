#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 0
def github() -> str:
    """
    This returns the link to my github repositoty
    """

    return "https://github.com/KaceyFranich/Kacey"
print(github())


# In[1]:


#Exercise 1
import pandas as pd

def read_data(year):
    """
    Create a list of the excel file names and an empty list for the data frames
    read each excel file and merge into one
    """
    file_names = ['https://lukashager.netlify.app/econ-481/data/ghgp_data_2022.xlsx', 'https://lukashager.netlify.app/econ-481/data/ghgp_data_2021.xlsx','https://lukashager.netlify.app/econ-481/data/ghgp_data_2020.xlsx','https://lukashager.netlify.app/econ-481/data/ghgp_data_2019.xlsx']
    data_frames = []
    for file_name in file_names:
        data_frames.append(pd.read_excel(file_name))
    merged_df = pd.concat(data_frames, ignore_index = True)
    return merged_df

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Using the merged excel files from above
    Skip the first 3 columns
    add a year column and append
    """
    dfs = []
    for year in years:
        df = read_data(year)
        df.columns = df.iloc[2] 
        df = df.iloc[3:] 
        df['year'] = year
        dfs.append(df)
        
    result_df = pd.concat(dfs, ignore_index=True)
    return result_df

years_of_data = [2019, 2020, 2021, 2022]
data = import_yearly_data(years_of_data)
print(data.head())
get_ipython().run_line_magic('store', 'data')


# In[5]:


#Exercise 2
import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    First we get the excel url and create an empty list to store the appended data
    Then we add a column for year
    Then remove rows that are entirely null values
    Then we append the original list with new data and concatenate into a dataframe
    I also had to change a column name for exercise 4
    """
    url = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'
    dfs_concat = []
    for year in years:
        parent_df = pd.read_excel(url, sheet_name = str(year), index_col = None)
        parent_df['year'] = year
        parent_df.dropna(axis=0, how='all', inplace=True)
        dfs_concat.append(parent_df)
        merged_df2 = pd.concat(dfs_concat, ignore_index = True)
    return merged_df2
years = [2019, 2020, 2021, 2022]
new_data = import_parent_companies(years)
new_data.rename(columns = {'GHGRP FACILITY ID':'Facility Id'}, inplace = True)
print(new_data.head())
get_ipython().run_line_magic('store', 'new_data')


# In[10]:


#Exercise 3
def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Find the number of null values in a given column
    use the isnull function to determine if a value in a column is null
    sum the null values
    lets use a sample dataframe to test this
    """
    null_bool = df[col].isnull()
    null_int = null_bool.sum()
    return null_int
my_df = pd.DataFrame({
    'A': [4, 1, None, 3],
    'B': [None, 4, 3, 2]
})
print(n_null(my_df, 'A'))


# In[9]:


#Exercise 4
import pandas as pd
get_ipython().run_line_magic('store', '-r data')
get_ipython().run_line_magic('store', '-r new_data')

emissions_df = data
parentco_df = new_data

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Start by merging to emissions and parent data sets, using 'on' to identify the join keys
    make a list of the selected columns
    combine the dataframes by the selected columns
    """
    combine_df = pd.merge(emissions_data, parent_data, on = ['year', 'Facility Id'], how = 'left')

    select_columns = ['Facility Id', 'year', 'State', 'Industry Type (sectors)',
                        'Total reported direct emissions', 'PARENT CO. STATE',
                        'PARENT CO. PERCENT OWNERSHIP']
    clean_df = combine_df[select_columns]
    clean_df.columns = clean_df.columns.str.lower()
    return clean_df

cleaned_result = clean_data(emissions_df, parentco_df)
print(cleaned_result.head()) 
get_ipython().run_line_magic('store', 'cleaned_result')


# In[32]:


#Exercise 5
get_ipython().run_line_magic('store', '-r cleaned_result')
def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    agg_functions = {
        'total reported direct emissions': ['min', 'median', 'mean', 'max'],
        'parent co. percent ownership': ['min', 'median', 'mean', 'max']
    }
    df['total reported direct emissions'] = pd.to_numeric(df['total reported direct emissions'], errors='coerce')
    df['parent co. percent ownership'] = pd.to_numeric(df['parent co. percent ownership'], errors='coerce')
    agg_data = df.groupby(group_vars, as_index=True).agg(agg_functions)

    agg_data = agg_data.sort_values(by=('total reported direct emissions', 'mean'), ascending=False, inplace = True)
    
    return agg_data

aggregated_data = aggregate_emissions(cleaned_result, group_vars=['state'])
print(aggregated_data)


# In[ ]:




