from django.test import TestCase

import requests

"""
 ||||||||||||  teste de l'api pour faire un url
"""

endpoint = "http://127.0.0.1:8000/api/load/"
headers = {
    "Content-Type": "application/json"
}

data = data={"url":endpoint}
# response = requests.post(endpoint, data={"url": endpoint})
response = requests.post(endpoint,json=data, headers=headers )

print(response)
