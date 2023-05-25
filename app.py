import os
import time
import requests


def make_api_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the returned data
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

# Example usage
api_url = "http://172.23.212.136:31856/api/todos"
result = make_api_request(api_url)
if result:
    print(result)