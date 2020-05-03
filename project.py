#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

headers = {
    'Ocp-Apim-Subscription-Key': "70160b67c389436d887e032b2958c6e2"
    }
query = {'q': 'Why the confusion about Kim Jong Un\'s health actually makes sense', 'textDecorations' : True}

response = requests.request("GET", url, headers=headers, params = query)

data = response.json()
data


# In[22]:




url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"

querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"10","q":"Why the confusion about Kim Jong Un","safeSearch":"false"}
''
headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())


# In[10]:


url = "https://jspell-checker.p.rapidapi.com/check"

payload = "{\t\"language\": \"enUS\",\t\"fieldvalues\": \"My lefe is beotifol\",\t\"config\": {\t\t\"forceUpperCase\": false,\t\t\"ignoreIrregularCaps\": false,\t\t\"ignoreFirstCaps\": true,\t\t\"ignoreNumbers\": true,\t\t\"ignoreUpper\": false,\t\t\"ignoreDouble\": false,\t\t\"ignoreWordsWithNumbers\": true\t}}"
headers = {
    'x-rapidapi-host': "jspell-checker.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196",
    'content-type': "application/json",
    'accept': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


# In[16]:


from IPython.display import display, Image
display(Image(filename='1643ki.jpg'))


# In[1]:


import pandas as pd
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_fake_news_websites')
data[2]


# In[2]:


import requests
import json
from IPython.display import display, HTML
import pandas as pd

def fake_news_sites_checker(link):
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_fake_news_websites')
    fake_sites = data[2]
    for site in fake_sites.to_records():
        if site['URL'] == link:
            return False

def test1(article):

    url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    headers = {
        'Ocp-Apim-Subscription-Key': "70160b67c389436d887e032b2958c6e2"
        }
    query = {'q': article, 'textDecorations' : True}

    response = requests.request("GET", url, headers=headers, params = query)

    data = response.json()

    data
    if data['webPages']['totalEstimatedMatches']!=0:
        link = data['webPages']['value'][0]['url']
        return link
    else:
        return False
    


display(HTML("<h1 style=color:DodgerBlue>Fake News Analyzer v1.0</h1>"))

data


# In[26]:


def test1(article):

    url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    headers = {
        'Ocp-Apim-Subscription-Key': "70160b67c389436d887e032b2958c6e2"
        }
    query = {'q': article, 'textDecorations' : True}

    response = requests.request("GET", url, headers=headers, params = query)

    data = response.json()

    data
    if data['webPages']['totalEstimatedMatches']!=0:
        link = data['webPages']['value'][0]['url']
        return link
    else:
        return False
    




# Example of the bad link
# 
# https://news.wow!@#$R%#.net

# In[ ]:





# In[ ]:




