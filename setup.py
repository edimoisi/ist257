
import requests
url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

headers = {
    'Ocp-Apim-Subscription-Key': "70160b67c389436d887e032b2958c6e2"
}
query = {'q': 'Why the confusion about Kim Jong Un\'s health actually makes sense',
         'textDecorations': True}

response = requests.request("GET", url, headers=headers, params=query)

data = response.json()
data

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI"

querystring = {"autoCorrect": "false", "pageNumber": "1", "pageSize": "10",
               "q": "Why the confusion about Kim Jong Un", "safeSearch": "false"}
''
headers = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "bf7b564eefmsh9551bdd7bdf2a65p123582jsne2cf6bbc1196"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())

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
