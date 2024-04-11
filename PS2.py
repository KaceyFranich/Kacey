#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 0
def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/KaceyFranich/Kacey"
print(github())


# In[8]:


#Exercise 1
import numpy as np
def simulate_data(seed: int) -> tuple:
    """
    First we generate xi1, xi2, xi3 using the numpy random normal generation function, with a mean of 0 and variance of 2. 
    Then we add the columns together to form X. 
    Then we generate the error term with the numpy random normal generation function, but with a variance of 1 instead of 2
    Then we can write the function for y
    """
    np.random.seed(seed)
    xi1 = np.random.normal(0, np.sqrt(2), size=(1000,))
    xi2 = np.random.normal(0, np.sqrt(2), size=(1000,))
    xi3 = np.random.normal(0, np.sqrt(2), size=(1000,))
    X = np.column_stack((xi1, xi2, xi3))

    e = np.random.normal(0, 1, size = 1000,)

    y = 5 + 3*xi1 + 2*xi2 + 6*xi3 + e
    return y.reshape(-1, 1), X

y, X = simulate_data(481)
print(y.shape)
print(X.shape)


# In[10]:


#Exercise 2
import numpy as np
import scipy as sp
#Log likelihood function
def neg_ll(parameters, y: np.array, X: np.array):
    """
    To do the MLE, first we need the log likelihood function
    """
    beta = np.array(parameters)
    mu = np.dot(X, beta[1:] + beta[0])
    ll = -.5*np.sum(np.log(2*np.pi)+(y-mu)**2)
    return -ll
    
def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    With the log likelihood function, we need to find the p value that maximizes the likelihood of observing the data. 
    This is done with the minimize function in scipy
    """
    starting_params = np.zeros(X.shape[1]+1)
    result = sp.optimize.minimize(neg_ll, starting_params, args = (y,X), method = 'Nelder-Mead')
    estimations = result.x
    return estimations

#Simulating the data 
np.random.seed(481)
xi1 = np.random.normal(0, np.sqrt(2), size=(1000,))
xi2 = np.random.normal(0, np.sqrt(2), size=(1000,))
xi3 = np.random.normal(0, np.sqrt(2), size=(1000,))
e = np.random.normal(0, 1, size=(1000,))
y = 5 + 3 * xi1 + 2 * xi2 + 6 * xi3 + e
X = np.column_stack(( xi1, xi2, xi3))

print(estimate_mle(y, X))

#Honestly not sure if I did this one right the estimations for the coefficients seem wrong


# In[8]:


#Exercise 3
import numpy as np
import scipy as sp

def estimate_ols(y: np.array, X: np.array):
    """
    use the np linear algebra function to estimate beta hat
    using the formula Beta hat = (X^TX)^1X^Ty
    """
    beta_hat = np.linalg.inv(X.T@X)@X.T@y
    return beta_hat

#Simulate the data
np.random.seed(481)
xi1 = np.random.normal(0, np.sqrt(2), size=(1000,))
xi2 = np.random.normal(0, np.sqrt(2), size=(1000,))
xi3 = np.random.normal(0, np.sqrt(2), size=(1000,))
ei = np.random.normal(0, 1, size=(1000,))
y = 5 + 3 * xi1 + 2 * xi2 + 6 * xi3 + ei
X = np.column_stack((np.ones_like(xi1),xi1, xi2, xi3))

print(estimate_ols(y, X))

