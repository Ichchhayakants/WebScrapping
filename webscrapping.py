#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the library used to query a website
import urllib.request


# In[2]:


#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"


# In[7]:


#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)


# In[5]:


#Import the beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup


# In[8]:


# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)


# In[9]:


print(soup.prettify)


# In[16]:


soup.title


# In[17]:


soup.title.string


# In[18]:


soup.a


# In[19]:


soup.find_all("a")


# In[20]:


all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))


# In[21]:


all_tables = soup.find_all('table')


# In[25]:


right_table = soup.find('table',class_='wikitable sortable plainrowheaders')


# In[26]:


print(right_table)


# In[28]:


right_table = soup.find('table',{"class":'wikitable sortable plainrowheaders'})
right_table


# In[31]:


A =[]
B =[]
C = []
D =[]
E = []
F =[]
G= []
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th') # tpo store second columns data
    if len(cells)==6: # Only extract table body no heading
        A.append(cells[0].find(text=True))
        B.append(cells[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))        


# In[32]:


# Import panda to onvert list to data
import pandas as pd
df = pd.DataFrame(A,columns =['Number'])
df['State/UT']= B
df['Admin_Capital'] =C
df['Legislative_Capital']=D
df['Judiciary_Capital'] =E
df['Year_Capital'] = F
df['Fomer_Capitals']=G
df


# In[ ]:





# In[ ]:




