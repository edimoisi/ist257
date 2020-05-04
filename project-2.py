#!/usr/bin/env python
# coding: utf-8

# In[41]:


import requests
url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

headers = {
    'Ocp-Apim-Subscription-Key': "70160b67c389436d887e032b2958c6e2"
    }
query = {'q': 'Why the confusion about Kim Jong Un\'s health actually makes sense', 'textDecorations' : True}

response = requests.request("GET", url, headers=headers, params = query)

data = response.json()
data


# In[14]:


import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"

querystring = {"autoCorrect":"false","pageNumber":"1","pageSize":"10","q":"Taylor Swift","safeSearch":"false"}

headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# In[22]:


url = "https://jspell-checker.p.rapidapi.com/check"

payload = "{\t\"language\": \"enUS\",\t\"fieldvalues\": \"My lefe is beotifol\",\t\"config\": {\t\t\"forceUpperCase\": false,\t\t\"ignoreIrregularCaps\": false,\t\t\"ignoreFirstCaps\": true,\t\t\"ignoreNumbers\": true,\t\t\"ignoreUpper\": false,\t\t\"ignoreDouble\": false,\t\t\"ignoreWordsWithNumbers\": true\t}}"
headers = {
    'x-rapidapi-host': "jspell-checker.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196",
    'content-type': "application/json",
    'accept': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

response = response.json()
response['spellingErrorCount']


# In[9]:


from IPython.display import display, Image
display(Image(filename='1643ki.jpg'))


# In[1]:


import pandas as pd
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_fake_news_websites')
data[2]


# In[42]:


import requests
import json
import IPython
import pandas as pd
from IPython.display import HTML

def spell_checker(article):
    url = "https://jspell-checker.p.rapidapi.com/check"

    payload = "{\t\"language\": \"enUS\",\t\"fieldvalues\":" +  "\"" + article + "\",\t\"config\": {\t\t\"forceUpperCase\": false,\t\t\"ignoreIrregularCaps\": false,\t\t\"ignoreFirstCaps\": true,\t\t\"ignoreNumbers\": true,\t\t\"ignoreUpper\": false,\t\t\"ignoreDouble\": false,\t\t\"ignoreWordsWithNumbers\": true\t}}"
    headers = {
        'x-rapidapi-host': "jspell-checker.p.rapidapi.com",
        'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196",
        'content-type': "application/json",
        'accept': "application/json"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    response = response.json()
    return response['spellingErrorCount']

def fake_news_sites_checker(link):
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_fake_news_websites')
    fake_sites = data[2]
    for site in fake_sites.to_records():
        if site['URL'] == link:
            return False

def news_search(article):

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

def link_checker(link):
    if link.find('.net') == -1 and link.find('.edu') == -1 and link.find('.com') == -1 and link.find('.info') == -1 and link.find('.io') == -1:
            return False
    forbidden_symbols = ['@', '~', '`', '?', '^', '!', '#', '$', '%', '&', '*', '(', ')', '{', '}', '[', ']']
    for character in link:
        if character not in forbidden_symbols:
            continue
        else:
            return False

def display_image(link):



    url = "https://zozor54-crawl-json-v1.p.rapidapi.com/getAllPictures"

    payload = "url=" + link
    headers = {
        'x-rapidapi-host': "zozor54-crawl-json-v1.p.rapidapi.com",
        'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    response = response.json()

    url = response[0]

    return IPython.display.Image(url, width = 250)

def users_input_welcome():
    print('Welcome to the Fake News Analyzer! What do you want to check?')
    print('1) Link')
    print('2) Article')
    proper_numbers = ['1', '2']
    while True:
        number = input('Enter the number ')
        if number not in proper_numbers:
            print('Sorry, try again\n')
            continue
        else:
            return number

def users_input_article():
    print('Paste the name or excerption from the article')
    print('1) Name')
    print('2) Excerption')
    proper_numbers = ['1', '2']
    while True:
        number = input('Enter the number ')
        if number not in proper_numbers:
            print('Sorry, try again\n')
            continue
        else:
            return number

def name_or_excerption(number):
    if number == '1':
        article = input('Put the name here ')
        return article
    
    elif number == '2':
        article = input('Put the excerption here ')
        return article
            

try:
    display(HTML("<h1 style=color:DodgerBlue>Fake News Analyzer v1.0</h1>"))
    while True:
        number = users_input_welcome()
        if number == '1':
            link = input('Enter your link ')
            if link_checker(link) == False:
                print('Your link is a fraud\n')
                answer = input('Do you want to check something else? (yes or no) ')
                if answer.lower().startswith('y'):
                    continue
                else:
                    print('Thank you for using our program')
                    break
            else:
                if fake_news_sites_checker(link) == False:
                    print('This website is fake\n')
                    answer = input('Do you want to check something else? (yes or no) ')
                    if answer.lower().startswith('y'):
                        continue
                    else:
                        print('Thank you for using our program')
                        break
                else:
                    print('It is a safe link. Enjoy your reading.')
                    answer = input('Do you want to check something else? (yes or no) ')
                    if answer.lower().startswith('y'):
                        continue
                    else:
                        print('Thank you for using our program')
                        break
        else:
            article_number = users_input_article()
            if article_number == '2':
                article = name_or_excerption(article_number)
                mistakes = spell_checker(article)
                if mistakes != 0:
                    print('This article is fake')
                    answer = input('Do you want to check something else? (yes or no) ')
                    if answer.lower().startswith('y'):
                        continue
                    else:
                        print('Thank you for using our program')
                        break
                else:
                    print('This article is safe. Enjoy your reading.')
                    answer = input('Do you want to check something else? (yes or no) ')
                    if answer.lower().startswith('y'):
                        continue
                    else:
                        print('Thank you for using our program')
                        break
            else:
                article = name_or_excerption(article_number)
                link = news_search(article)
                if link != False:
                    print('Article is safe. Below you can find a link to read it.')
                    
                    print(link)
                    print()
                    answer = input('Do you want to check something else? (yes or no) ')
                    if answer.lower().startswith('y'):
                        continue
                    else:
                        print('Thank you for using our program')
                        break
                else:
                    print('This article is fake.')
                    answer = input('Do you want to check something else? (yes or no) ')
                    if answer.lower().startswith('y'):
                        continue
                    else:
                        print('Thank you for using our program')
                        break
            
            
except IndexError as e:
    print()
    display(HTML("<h1>Sorry we could not find your article.</h1>"))
except requests.exceptions.HTTPError as f:
    print()
    display(HTML("<h1>Oops. Something went wrong.</h1>"))
except TypeError as m:
    print()
    display(HTML("<h1>Sorry we could not find your article.</h1>"))


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
    




# In[36]:


import IPython

url = "https://zozor54-crawl-json-v1.p.rapidapi.com/getAllPictures"

payload = "url=" + link
headers = {
    'x-rapidapi-host': "zozor54-crawl-json-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

response = response.txt()

response


# Example of the bad link
# 
# https://news.wow!@#$R%#.net

# In[39]:


import requests

url = "https://zozor54-crawl-json-v1.p.rapidapi.com/getAllPictures"

payload = "url=https%3A%2F%2Fwww.sendrank.com"
headers = {
    'x-rapidapi-host': "zozor54-crawl-json-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

response = response.json()
response
display_image(link)


# In[ ]:




