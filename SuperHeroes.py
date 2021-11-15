import requests
from pprint import pprint
import json

def who_smart(heroes):
    heroes_dict = {}
    intelligence = 0
    hero_name = ''
    for superhero in heroes:
        url = "https://superheroapi.com/api/2619421814940190/search/"+superhero
        response = requests.get(url)
        response_outfit = response.json()
        heroes_dict[superhero] = int(response_outfit['results'][0]['powerstats']['intelligence'])
        if heroes_dict[superhero] > intelligence:
            intelligence = heroes_dict[superhero]
            hero_name = superhero
    print(f'Самый умный {hero_name}')

who_smart(['Thanos', 'Hulk', 'Captain America'])

def upload_file(token):
    headers = {
        "Accept": "application/json",
        "Authorization": "OAuth " + token
    }

    params = {
        'path':f"Python/Ferrari_2.jpg",
        'overwrite':True
    }

    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    response = requests.get(url=url, params=params, headers=headers)
    result = response.json()
    print(json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False))
    upload = requests.put(url=result['href'], data=open('/Users/keeeril/Downloads/Ferrari_2.jpg', 'rb'), params=params, headers=headers)
    print(upload.status_code)

upload_file("")
