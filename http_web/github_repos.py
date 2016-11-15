#!/usr/bin/env python3

import requests

response = requests.get('https://api.github.com/users/cnzau/repos')

assert response.status_code == 200

for repo in response.json():
    print (repo['name'], '\t\t\t\t', repo['language'])