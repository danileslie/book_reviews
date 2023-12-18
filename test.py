import requests


param = {
    'fantastic fox'
}
response = requests.get("https://openlibrary.org/search.json", params=param)
book = response.json()

print(book)