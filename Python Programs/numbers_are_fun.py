import json
import requests

number = input('Enter a number: ')
url = 'http://numbersapi.com/' + number

print(requests.get(url).text)
