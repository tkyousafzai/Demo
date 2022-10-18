import requests
import json
# url="https://openlibrary.org/authors/OL23919A.json"
url = "https://openlibrary.org/search/authors.json?q= Olivia Jo Murray" # get data bases on author name
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent = 4, sort_keys=True)
print(content)


#The output of the API call can be stored in panda dataframe,CSV or parquet file format for tranformations or getting the any desired information
