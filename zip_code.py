#!/usr/bin/env python3
# Zip Code Mile Calculator | Copyright Justin Snyder

import requests
api_key = 'fbGZ0HhCVnqqKte9Bnfwlo1xt3ONw0eLbVLcC3OxqeYaIdkjAAQWYSusVifsiuet'


def get_distance(zip1, zip2):
    url = 'http://www.zipcodeapi.com/rest/' + api_key + \
        '/distance.json/' + str(zip1) + '/' + str(zip2) + '/mile'
    r = requests.get(url)
    if r.status_code >= 300:
        print('got a strange error ' + r.text)
        return 0.0
    json = r.json()
    return json['distance']


print('Welcome to the Zip Code Mile Calcualtor')
ans = input('Are you ready to begin? type yes or no!')
if ans.lower() == 'yes' or ans.lower() == 'y':
    strt = input('Enter Start Zip Code')  # Enter Starting Zip Code
    end = input('Enter End Zip Code')  # Enter Ending Zip Code
    dist = get_distance(strt, end)
    print('The estimated miles from', strt, 'to', end, 'is', dist)
else:
    print('Thanks For Trying')
