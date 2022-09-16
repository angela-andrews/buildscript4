#!/usr/bin/env python3
# this is a test for build script 4
# I was trying to figure out how to use python
# for the api query
import requests

url = "https://v1.basketball.api-sports.io/games?h2h=154-153"

payload={}
headers = {
  'x-rapidapi-key': 'c9d1a76cf2118df18d8d324a8de4e101',
  'x-rapidapi-host': 'v1.basketball.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

