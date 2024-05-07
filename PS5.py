#!/usr/bin/env python
# coding: utf-8

# In[14]:


def github() -> str:
    """
    Function that returns link to my github
    """

    return "https://github.com/KaceyFranich/Kacey"

github()


# In[12]:


import requests
from bs4 import BeautifulSoup
import re

def scrape_code(url: str) -> str:
    """
    First, I get the webpage content using requests.get
    Then I parse it using BeautifulSoup and filtered out the IPython magic commands
    Then I search the html by 'sourceCode Python' to find all the python code in the lecture
    I included an if statement to skip ipython magic commands or empty lines of code
    Then joined all the code lines into a single string
    """
    webpage = requests.get(url)
    webpage.raise_for_status()
        
    soup = BeautifulSoup(webpage.content, 'html.parser')
    ipython_magic_pattern = re.compile(r'^\s*%')
        
    python_code_lines = []
    for element in soup.find_all(['p', 'pre', 'code']):
            
        code_snippet = element.get_text().strip()
            
        if not code_snippet or ipython_magic_pattern.match(code_snippet):
            continue
            
        lines = code_snippet.split('\n')
        for line in lines:
            if not ipython_magic_pattern.match(line.strip()):
                python_code_lines.append(line.strip())

    python_code = '\n'.join(python_code_lines)
    return python_code

lecture_url = "https://lukashager.netlify.app/econ-481/01_intro_to_python"
lecture_code = scrape_code(lecture_url)
print(lecture_code)


# In[ ]:




