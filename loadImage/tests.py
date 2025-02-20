from django.test import TestCase

import requests

"""
 ||||||||||||  teste de l'api pour faire un url
"""

endpoint = "http://127.0.0.1:8000/api/load/"
headers = {
    "Content-Type": "application/json"
}
url = "https://miniamaker.ai/"
url = "https://flutter.dev/"

data = data={"url":url}
# response = requests.post(endpoint, data={"url": endpoint})
response = requests.post(endpoint,json=data, headers=headers )

print(len(response.content))
print(response.status_code)