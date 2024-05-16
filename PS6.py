#!/usr/bin/env python
# coding: utf-8

# In[15]:


def github() -> str:
    """
    Returns a link to my github
    """

    return "https://github.com/KaceyFranich/Kacey"

github()


# In[10]:


import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

path = 'auctions.db'

class DataBase:
    def __init__(self, loc: str, db_type: str = "sqlite") -> None:
        """Initialize the class and connect to the database"""
        self.loc = loc
        self.db_type = db_type
        self.engine = create_engine(f'{self.db_type}:///{self.loc}')
    def query(self, q: str) -> pd.DataFrame:
        """Run a query against the database and return a DataFrame"""
        with Session(self.engine) as session:
            df = pd.read_sql(q, session.bind)
        return(df)
        
auctions = DataBase(path)

def std() -> str:
    """
    Begin by selecting the required columns
    then calculating the standard deviation using the formula given
    then joins table on itemid, and group by itemids with at least 2 bids
    """
    query = """
    select items.itemId, 
           sqrt(sum((bids.bidamount - avg(bids.bidamount) * (bids.bidamount - avg(bids.bidamount)) / (count(bids.ItemId) - 1))) as std
    from items
    join bids on items.itemId = bids.itemId
    group by items.itemId
    having count(bids.bidamount) >= 2;
    """
    return query

print(std())


# In[3]:


def bidder_spend_frac() -> str:
    """
    Begins by selecting the required columns
    The sum of the winning bids at total_spend
    the max of the bidamount as total bids
    and total spend/total bids as spend frac
    Then join by the bidderID
    """
    query = """
    select bids.bidderName,
           sum(case when bids.outcome = 'winning' then bids.bidamount else 0 end) as total_spend,
           max(bids.bidamount) as total_bids,
           round(total_spend) / bids.bidamount, 2) as spend_frac
    from bidders
    join bids ON bids.bidderId = bids.bidderId
    group by bids.biddername;
    """
    return query

print(bidder_spend_frac())


# In[1]:


def min_increment_freq() -> str:
    """
    Start by selecting the calulated column for frequency, which is the fraction of bids in the database that are exactly the minimum bid increment
    above the previous high bid
    Then join on itemids 
    and use items.isbuynowused = 0 to exlude the items where isbuynowused = 1
    """
    sql_query = """
    select cast(sum(case when bids.bidamount = (items.currentBid + items.bidIncrement) then 1 else 0 end) as real) / count(*) as freq
    from bids 
    join items ON bids.itemId = items.itemId
    where items.isBuyNowUsed = 0
    and bids.bidamount > items.currentBid
    """

    return sql_query

print(min_increment_freq())


# In[12]:


def win_perc_by_timestamp() -> str:
    """
    using 10 bins to categorize by the percentage of time remaining in the auction when a bid is placed
    determine if the bid is a winning bid by seeing if it matches the current highest bid 
    group by the timesdtamp bid, using the avg of 'is winner' to find the win percentage
    Then order by timestamp_bin
    """
    sql_query = """
    With TimeBins as (
        select
            (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) as timestamp_norm,
            case
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.1 then 1
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.2 then 2
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.3 then 3
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.4 then 4
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.5 then 5
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.6 then 6
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.7 then 7
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.8 then 8
                when (julianday(bids.timestamp) - julianday(items.startTime)) / (julianday(items.endTime) - julianday(items.startTime)) <= 0.9 then 9
                else 10
            end as timestamp_bin,
            case when bids.bidamount = items.currentBid then 1 else 0 end as is_winner
        from bids 
        join items on bids.itemId = items.itemId
        where items.isBuyNowUsed = 0
    )
    select timestamp_bin, avg(is_winner) as win_perc
    from TimeBins
    group by timestamp_bin
    order by timestamp_bin
    """

    return sql_query

print(win_perc_by_timestamp())


# In[ ]:




