import requests

url = r"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={}&format=json&limit=50&formatversion=2&language=en".format("baseball")
r = requests.post(url)

print(r.json()["search"][49]["label"] )



