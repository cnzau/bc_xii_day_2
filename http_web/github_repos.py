#!/usr/bin/env python3

import requests
print("Console app to print github repositories and languages used")

user = input("Enter your GitHub Username: ")

if user == None:
	print("User not provided!")
	
response = requests.get('https://api.github.com/users/%s/repos' % user)

assert response.status_code == 200

for repo in response.json():
    print(repo['name'], '\t\t\t\t', repo['language'])
